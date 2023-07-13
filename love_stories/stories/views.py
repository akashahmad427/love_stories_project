from django.shortcuts import render
from django.contrib import messages
from . models import Data
from .forms import Firstform
# Create your views here.
def home(request):
    return render(request,'stories/home.html')

#stories page view function
def stories(request):
    fm = Data.objects.all()
    return render(request,'stories/stories.html',{'form':fm})

# form to fetch data from user
def add_story(request):
    if request.method == 'POST':
        fm = Firstform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Congratulations ! Your story has been successfully uploaded')
    else:
        fm = Firstform()
    return render(request,'stories/add_story.html',{'form':fm})
#about page 
def about(request):
    return render(request,'stories/about.html')
