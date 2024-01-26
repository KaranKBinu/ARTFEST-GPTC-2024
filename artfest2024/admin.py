from django.contrib import admin
from .models import Programs, StudentDetails, StudentUsers, ContactMessage
from django.contrib import admin
from .models import StudentUsers, Notification
from .admin_actions import export_to_excel

# admin.py


@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ["student_name", "admn_no", "branch", "sem"]
    list_filter = ["house", "branch", "sem"]
    search_fields = [
        "student_name",
        "admn_no",
    ]  # Make sure these fields exist in your model


class StudentUsersAdmin(admin.ModelAdmin):
    list_display = (
        "student_admn_no",
        "student_name",
        "student_email",
        "student_phone",
        "house_name",
        "Gender",
    )
    list_filter = (
        "house_name",
        "Gender",
        "program",
    )  # Add these lines to enable filtering
    actions = [export_to_excel]


admin.site.register(StudentUsers, StudentUsersAdmin)


admin.site.register(Programs)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")


admin.site.register(ContactMessage, ContactMessageAdmin)


admin.site.register(Notification)
