from django.db import models
from artfest2024.models import StudentUsers, Programs


class Stage(models.Model):
    stage_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.stage_name


class Attendance(models.Model):
    PERIOD_CHOICES = [
        (1, "Period 1"),
        (2, "Period 2"),
        (3, "Period 3"),
        (4, "Period 4"),
        (5, "Period 5"),
        (6, "Period 6"),
    ]

    student_admn_no = models.CharField(max_length=4, default="")
    period = models.IntegerField(choices=PERIOD_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    attendance = models.BooleanField()
    co_ordinator = models.CharField(max_length=255)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, default="")
    program = models.ForeignKey(Programs, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.student_admn_no} - {self.stage} - {self.attendance}"


class Co_ordinator(models.Model):
    co_ordinator_name = models.CharField(max_length=255)
    co_ordinator_email = models.EmailField()
    program = models.ForeignKey(Programs, on_delete=models.CASCADE)
    user_name_for_coordinator = models.CharField(max_length=255, default="")
    password_for_coordinator = models.CharField(max_length=255, default="")
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.co_ordinator_name} - {self.program}"
