from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cal(request):
    return render(request,'calculator/cal.html')