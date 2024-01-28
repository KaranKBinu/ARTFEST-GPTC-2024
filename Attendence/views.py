from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Co_ordinator, Attendance, Stage
from artfest2024.models import StudentUsers

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Co_ordinator, Attendance, Stage
from artfest2024.models import StudentUsers


def attendence_index(request):
    # Check if the user is authenticated
    if "coordinator_username" in request.session:
        # Retrieve attendance data from the database
        coordinator_username = request.session.get("coordinator_username")
        print(coordinator_username)

        # Retrieve the coordinator object
        coordinator = Co_ordinator.objects.get(
            user_name_for_coordinator=coordinator_username
        )
        program_of_coordinator = coordinator.program

        student_data = StudentUsers.objects.filter(program=program_of_coordinator)
        print(student_data)

        if request.method == "POST":
            # Process the attendance form submission
            period = request.POST.get("period")
            stage_id = request.POST.get("stage")
            stage = Stage.objects.get(id=stage_id)
            for student in student_data:
                attendance_status = request.POST.get(
                    f"attendance_{student.student_admn_no}",
                )

                if attendance_status == "1":
                    # Assuming the form field names are like 'attendance_<student_admn_no>'
                    attendance = Attendance.objects.create(
                        student_admn_no=student.student_admn_no,
                        period=period,
                        attendance=True,
                        co_ordinator=coordinator_username,
                        stage=stage,
                        program=program_of_coordinator,
                    )
                    attendance.save()

        stages = Stage.objects.all()
        context = {
            "student_data": student_data,
            "stages": stages,
            "PERIOD_CHOICES": Attendance.PERIOD_CHOICES,
            "program_of_coordinator": program_of_coordinator,
            "coordinator": coordinator,
        }

        return render(request, "attendence_index.html", context)
    else:
        return redirect("attendence_login")


def attendence_login(request):
    if request.method == "POST":
        co_ordinator_username = request.POST.get("coordinator_username")
        co_ordinator_password = request.POST.get("coordinator_password")

        # Manually check the username and password
        try:
            user = Co_ordinator.objects.get(
                user_name_for_coordinator=co_ordinator_username
            )

            if user.password_for_coordinator == co_ordinator_password:
                # Set session variable to indicate user is logged in
                request.session["coordinator_username"] = co_ordinator_username
                # Redirect to a success page or home page
                messages.success(request, "Co-ordinator login success")
                return redirect("attendence_index")
            else:
                messages.error(request, "Invalid credentials. Please try again.")
                print("error 1")
        except Co_ordinator.DoesNotExist:
            print("error 2")
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, "attendence_login.html")


def attendence_logout(request):
    # Remove the session variable to indicate user is logged out
    if "coordinator_username" in request.session:
        del request.session["coordinator_username"]
        messages.success(request, "Co-ordinator logout success")
    return redirect("attendence_login")
