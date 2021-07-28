from django.shortcuts import render
from base_app import views
# Create your views here.
def index(request):
    return render(request,'base_app/index.html')

def others(request):
    return render(request,'base_app/others.html')

def relative(request):
    return render(request,'base_app/relative_turls.html')
