from django.shortcuts import render


# Create your views here.
def attendence_index(request):
    return render(request, "attendence_index.html")
