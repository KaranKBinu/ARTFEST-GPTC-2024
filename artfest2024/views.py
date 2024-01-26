from django.http import HttpResponse, HttpResponseRedirect
from .models import Notification, Programs, StudentUsers
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import StudentUsers, StudentDetails
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import ContactMessage


def get_common_data():
    return {"AllStudents": StudentDetails.objects.all()}


def user_logout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect("index")


def user_login(request):
    if request.method == "POST":
        student_admn_no = request.POST.get("student_admn_no")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=student_admn_no, password=password)

        if user is not None:
            request.session["user_admn_no"] = student_admn_no
            # Login the user
            login(request, user)

            # Redirect to the select_categories view or any other desired page
            messages.success(request, "Login Success")
            return redirect("select_categories")
        else:
            # Authentication failed, show an error message
            messages.error(request, "Invalid admission number or password.")

    # If the request is not a POST or authentication fails, render the login page
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        student_admn_no = request.POST.get("student_admn_no")
        student_name = request.POST.get("student_name")
        student_email = request.POST.get("student_email")
        student_phone = request.POST.get("student_phone")
        student_password = request.POST.get("student_password")
        confirm_password = request.POST.get("confirm_password")
        Gender = request.POST.get("gender")
        house_name = StudentDetails.objects.get(admn_no=student_admn_no).house
        if User.objects.filter(email=student_email).exists():
            messages.error(request, "email already exists")
            return redirect(index)
        # Check if the student admission number already exists in StudentDetails
        if not StudentDetails.objects.filter(admn_no=student_admn_no).exists():
            messages.error(
                request,
                "Admission number incorrect. Please use a different admission number.",
            )
            return render(request, "index.html", {"messages": messages})

        if student_password == confirm_password:
            # Check if the user with the given email already exists
            if User.objects.filter(email=student_email).exists():
                messages.error(
                    request, "Email already exists. Please use a different email."
                )
                return render(
                    request, "index.html", {"messages": messages, **get_common_data()}
                )

            # Create a new User instance (Django User model)
            if User.objects.filter(username=student_admn_no).exists():
                messages.error(request, "Admission Number already exists")
                return redirect("index")
            else:
                user = User.objects.create_user(
                    username=student_admn_no,
                    email=student_email,
                    password=student_password,
                )

            student = StudentUsers.objects.create(
                student_admn_no=student_admn_no,
                student_name=student_name,
                student_email=student_email,
                student_phone=student_phone,
                student_password=student_password,
                house_name=house_name,
                Gender=Gender,
            )

            # Link the user to the student profile
            student.user = user
            student.save()

            # Authenticate the user
            auth_user = authenticate(
                request, username=student_admn_no, password=student_password
            )
            if auth_user:
                login(request, auth_user)
                request.session["user_admn_no"] = student_admn_no

            return redirect(select_categories)
        else:
            messages.error(request, "Passwords do not match.")
    else:
        Allstudents = StudentDetails.objects.all()
        return render(
            request, "index.html", {"Allstudents": Allstudents, "messages": messages}
        )
    return render(
        request, "index.html", {"Allstudents": Allstudents, "messages": messages}
    )


@login_required(login_url="index")
def select_categories(request):
    user_admn_no = request.session.get("user_admn_no")
    if user_admn_no is not None:
        userdetails = StudentUsers.objects.get(student_admn_no=user_admn_no)
        programs = Programs.objects.all()
    else:
        messages.error(
            request,
            "may Be there is an Error occured while Authentication,Try Refreshing",
        )
        return redirect("index")
    if request.method == "POST":
        selected_programs = request.POST.getlist("selected_programs")
        with transaction.atomic():
            # Clear the existing programs for the user
            userdetails.program.clear()

            # Add the selected programs to the user
            selected_program_details = []
            for program_name in selected_programs:
                program = Programs.objects.get(program_name=program_name)
                userdetails.program.add(program)
                selected_program_details.append(
                    {
                        "program_name": program.program_name,
                        "program_code": program.program_code,
                        "chess_no": program.program_code + user_admn_no,
                    }
                )

            # Send email to the user using Gmail's SMTP server
            subject = "Arts Fest 2024"
            context = {
                "userdetails": userdetails,
                "selected_program_details": selected_program_details,
            }
            html_message = render_to_string("email_template.html", context)
            plain_message = strip_tags(html_message)
            from_email = (
                settings.DEFAULT_FROM_EMAIL
            )  # Use the sender email from your Django settings

            recipient_list = [userdetails.student_email]

            send_mail(
                subject,
                plain_message,
                from_email,
                recipient_list,
                html_message=html_message,
            )

            messages.success(
                request,
                "Program choices updated successfully and an email sent to your registered email.",
            )

    return render(
        request,
        "select-categories.html",
        {"userdetails": userdetails, "programs": programs, **get_common_data()},
    )


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save the form data to the database
        ContactMessage.objects.create(
            name=name,
            telephone=telephone,
            email=email,
            subject=subject,
            message=message,
        )

        # You can redirect to a thank you page or any other desired page
        messages.success(request, "Thank You For contacting Us")
        return redirect("index")

    return redirect("index")  # Replace with your actual template name


# def index(request):
#     return redirect("https://artsfest2024gptccherthala.xyz/")
def index(request):
    messages.success(request, "welcome")
    notifications = Notification.objects.filter(is_shown=True)
    return render(
        request, "index.html", {**get_common_data(), "notifications": notifications}
    )


def categories(request):
    categories = Programs.objects.all()
    return render(
        request, "categories.html", {"categories": categories, **get_common_data()}
    )


def contests(request):
    return render(request, "contests.html", get_common_data())


from django.shortcuts import render
from .models import StudentUsers, Programs


def contest_details(request):
    # Get the filter parameters from the request
    house_filter = request.GET.get("house", "")
    program_filter = request.GET.get("program", "")

    # Filter students based on house and program_name
    students = StudentUsers.objects.all()
    if house_filter:
        students = students.filter(house_name=house_filter)
    if program_filter:
        students = students.filter(program__program_name=program_filter)

    # Get all distinct house names and program names for filtering options
    houses = StudentUsers.objects.values_list("house_name", flat=True).distinct()
    programs = Programs.objects.values_list("program_name", flat=True).distinct()

    context = {
        "students": students,
        "houses": houses,
        "programs": programs,
        "selected_house": house_filter,
        "selected_program": program_filter,
        **get_common_data(),
    }

    return render(request, "contest_details.html", context)


# def upload_and_process_excel(request):
#     if request.method == 'POST' and request.FILES['excel_file']:
#         excel_file = request.FILES['excel_file']
#         # Read Excel file into a pandas DataFrame
#         df = pd.read_excel(excel_file)
#         output_filepath = 'out2.json'
#         with open(output_filepath, 'w') as file:
#             for student_data in df.to_dict(orient='records'):
#                 file.write(str(student_data) + '\n')
#     else:
#         return render(request,'upload_excel.html')
#     return HttpResponse("<h2>Insertion Success</h2>")
