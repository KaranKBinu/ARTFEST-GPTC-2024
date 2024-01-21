from django.db import models


class StudentDetails(models.Model):
    student_name = models.CharField(max_length=255)
    admn_no = models.CharField(max_length=4)
    Gender = models.CharField(max_length=20,default='Male')
    branch = models.CharField(max_length=255)
    sem = models.CharField(max_length=4)
    house=models.CharField(max_length=255)


    def __str__(self):
        return f"{self.student_name} - {self.admn_no}"

class Programs(models.Model):
    PROGRAM_CHOICES = (
        ('individual', 'individual'),
        ('Group','Group'),
    )
    GENDER_CHOICES=(
        ("male", "Male"),
        ("female","Female"),
        ("all","All"),
    )
    STAGE_CHOICES=(
        ("On-Stage","On-Stage"),
        ("Off-Stage","Off-Stage"),
    )
    program_code = models.CharField(max_length=88)
    program_name = models.CharField(max_length=255)
    program_type = models.CharField(max_length=255,choices=PROGRAM_CHOICES)
    Gender_choices = models.CharField(max_length=255,choices=GENDER_CHOICES)
    Stage_choices = models.CharField(max_length=255,choices=STAGE_CHOICES)

    def __str__(self):
        return self.program_name
    
class StudentUsers(models.Model):
    student_admn_no = models.CharField(max_length=4)
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=10)
    student_password = models.CharField(max_length=255)
    house_name = models.CharField(max_length=255)
    Gender=models.CharField(max_length=20)
    program = models.ManyToManyField(Programs)

    def __str__(self):
        return f"{self.house_name} - {self.student_admn_no}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Name : {self.name} - Subject :{self.subject}"