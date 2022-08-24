# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import messages
from hostel.models import Hostelite,Register
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    return render(request,'landing/home.html')

def signin(request):
    if request.method == 'POST':
        sic = request.POST.get("sic")
        password = request.POST.get("password")
        print(sic)
        user = authenticate(request,username=sic,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('matcher')
        else:
            messages.error(request,"invalid credentials")

        

    return render(request,'landing/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

def signup(request):
    if request.method=='POST':
        sic = request.POST.get("sic")
        password = request.POST.get("password")
        desc = request.POST.get("desc")
        hobby = request.POST.get("hobby")

        hostelite = Hostelite.objects.filter(sic=sic)
        register = Register.objects.filter(sic=sic)
        if register.exists():
            print("exists")
            messages.error(request,"Already Registered")
            return render(request,'landing/signup.html')
        
        if not hostelite.exists():
            print("not in database")
            messages.error(request,"User not in Database")
            return render(request,'landing/signup.html')

        else:
            try:
                user_dict= hostelite.values()[0]
                print(user_dict)
                print(user_dict['first_name'])
                
                user = User.objects.create_user(
                    first_name = user_dict['first_name'],
                    last_name = user_dict['last_name'],
                    username = user_dict['sic'],
                    email = user_dict['email'],
                    password = password
                )
                user.save()

                regi = Register.objects.create(
                    sic = Hostelite.objects.get(sic=sic),
                    user = User.objects.get(username=sic),
                    desc = desc,
                    hobby = hobby
                )
                regi.save()
            
            except Exception as e:
                print(e)

        return redirect('signin')
   



    return render(request,'landing/signup.html')