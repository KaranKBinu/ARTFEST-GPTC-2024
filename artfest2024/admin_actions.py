import csv
from openpyxl import Workbook
from django.http import HttpResponse

def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students_data.xlsx'

    workbook = Workbook()
    worksheet = workbook.active

    # Add headers to the worksheet
    headers = [
        'Admission Number',
        'Name',
        'Email',
        'Phone',
        'Password',
        'House Name',
        'Gender',
        'Programs',
    ]
    for col_num, header in enumerate(headers, 1):
        worksheet.cell(row=1, column=col_num, value=header)

    # Add data to the worksheet
    for row_num, student in enumerate(queryset, 2):
        worksheet.cell(row=row_num, column=1, value=student.student_admn_no)
        worksheet.cell(row=row_num, column=2, value=student.student_name)
        worksheet.cell(row=row_num, column=3, value=student.student_email)
        worksheet.cell(row=row_num, column=4, value=student.student_phone)
        worksheet.cell(row=row_num, column=5, value=student.student_password)
        worksheet.cell(row=row_num, column=6, value=student.house_name)
        worksheet.cell(row=row_num, column=7, value=student.Gender)
        programs = ', '.join(str(program) for program in student.program.all())
        worksheet.cell(row=row_num, column=8, value=programs)

    workbook.save(response)
    return response

export_to_excel.short_description = "Export selected students to Excel"

