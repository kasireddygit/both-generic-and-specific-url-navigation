from django.shortcuts import render

# Create your views here.

def response1(request):
    return render(request,'response1.html')

def response2(request):
    return render(request,'response2.html')