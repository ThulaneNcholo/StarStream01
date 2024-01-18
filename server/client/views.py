from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def LandingPage(request):
    return render(request,'client/landingPage.html')

def IndexView(request):
    celebs = CelebritiesModel.objects.all()

    context = {
        "celebs" : celebs
    }
    return render(request,'client/index.html',context)

def CategoryResults(request):
    celebs = CelebritiesModel.objects.all()

    context = {
        "celebs" : celebs
    }

    return render(request,'client/category.html',context)

def Profile(request,id):
    celeb = CelebritiesModel.objects.get(id = id)

    context = {
        "celeb" : celeb
    }

    return render(request,'client/profile.html',context)

def UserProfile(request):
    return render(request,'client/user_profile.html')

def TrendingCelebs(request):
    celebs = CelebritiesModel.objects.all()

    context = {
        "celebs" : celebs
    }

    return render(request,'client/trendingPage.html',context)


def SignUpPage(request):

    if request.method == 'POST' and 'submit_signUp' in request.POST:
        
        saveUser = SignUpsModel()
        saveUser.first_name = request.POST.get('firstName')
        saveUser.last_name = request.POST.get('lastName')
        saveUser.email = request.POST.get('email')
        saveUser.status = request.POST.get('options')
        saveUser.save()

        return redirect('complete')
  
    return render(request,'client/signUp_page.html')

def successfulPage(request):
    return render(request,'client/successfullPage.html')
