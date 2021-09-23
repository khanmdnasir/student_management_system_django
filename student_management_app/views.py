from django.shortcuts import render

# Create your views here.
def demoview(request):
    return render(request,'student_management_app/demo.html')