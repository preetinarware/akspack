
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout ,login,authenticate
import uuid

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from numpy import require
from .models import *
# Create your views here.


def usr_register(request):
    try:
        if request.method=='POST':
            try:
                if request.POST['email']!='' and request.POST['username']!='' and request.POST['password']!='':
                
                    if len(User.objects.filter(username=request.POST.get('username')))==1 :    
                        return render(request,'register.html',{'error':'Username has already been taken.'})
                    if  len(User.objects.filter(email=request.POST.get('email')) )==1:
                            return render(request,'register.html',{'error':'Email has already been taken.'})

                    user=User.objects.create_user(username=request.POST['username'],
                    email=request.POST['email'],password=request.POST['password'])
                    token=str(uuid.uuid4())
                    frgpwd=frgt_pwd(user=user,frg_token=token)
                    frgpwd.save()  
                    messages.success(request,'Registraion successfully.Please Login !')
                    return redirect('login')
                else:
                    return render(request,'register.html',{'error':'All field required !'})
        
            except Exception as e:
                print('user not exit',e)

    except Exception as e:
            print('user not exist',e)
    return render(request,'register.html')

def usr_login(request):
    
    # nxt=request.META.get('HTTP_REFERER')
    # print(nxt,'ooooooo',request.get_full_path())
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        if request.method=='POST':
                email = request.POST['email']
                password = request.POST['password']
                nxt=request.POST['next']
        
                try:  
                    if email!='' and password!='':
                            username = User.objects.get(email=email).username       
                            user = authenticate(request, username = username, password = password)
                            if user is not None:
                                login(request, user)
                                messages.success(request, f' Welcome {username}.')
                                if nxt == request.get_full_path() or nxt =='forgot-password' or nxt=='password-confirm/<str:id>/':
                                    print('ppp')
                                    return redirect('home')
                                elif nxt != request.get_full_path():
                                    print('iii')
                                    return redirect(nxt)
                            else:
                                return render(request,'login.html',{'error':'Invalid email or password !'})
                    
                    else:
                        return render(request,'login.html',{'error':'Both field are required.'})
                                # messages.info(request, f'account dose not exit plz sign up')
                except User.DoesNotExist:
                    print('invalid')
                    return render(request,'login.html',{'error':'Invalid user.'})

    return render(request,'login.html')


@login_required(login_url='login')
def usr_logout(request):
    try:
        logout(request)
        messages.success(request,'Logout Successfully.')
        return redirect('home')
    except Exception as e:
        print(e)
   
def frgt_pass(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
    
        try :
                if request.method=='POST':
                        email=request.POST['email']
                        if User.objects.filter(email=email):
                            useremail=User.objects.get(email=email)
                            ftoken=frgt_pwd.objects.get(user=useremail).frg_token
                            emails=useremail.email 
                            # mail_msg=f'Your reset password link is https://akspckage2022.herokuapp.com/password-confirm/{ftoken}.'
                            mail_msg=(f'Set Password \n Your reset password link is http://127.0.0.1:8000/password-confirm/{ftoken}.')
                            send_mail('Forgot Password', mail_msg,settings.EMAIL_HOST_USER,[emails],fail_silently=False)
                            messages.success(request, "Mail Send Successfully.\n Please Check Your Email.")
                            return redirect('forgot-password')
                        else:
                            print('user none')
                    #          msg1=(f'\n\n Name :  {name} \n Email :  {email} \n Message :  {msg}')
                    # send_mail(subject,msg1,email,[settings.EMAIL_HOST_USER],fail_silently=False)
                    
                            # messages.error(request,'Invalid ! Email.')
                            return render(request,'forgot-password.html',{'error':'Invalid email !'})
        except Exception as e:
            print(e)
        return render(request,'forgot-password.html')




def pwd_reset_cnfrm(request,id):
    # if request.user.is_authenticated!=True:
    if request.user.is_authenticated:
        return redirect ('home')
    else:
    
        try:
            if request.method=='POST':
                pass1=request.POST['password']
                confirm=request.POST['confirm']
                if pass1!='' and confirm !='':
                    if pass1==confirm:
                        frgpwd=frgt_pwd.objects.get(frg_token=id)
                        user=User.objects.get(username=frgpwd)
                        user.set_password(pass1)
                        user.save()
                        messages.success(request, "Password Change Successfully. ")
                        return redirect('login')
                    else:
                        return render(request,'pwd-reset-confirm.html',{'error':'Password not match !'})
                else:
                        return render(request,'pwd-reset-confirm.html',{'error':'Both field required !'})
        except Exception as e:
            print(e)
        return render(request,'pwd-reset-confirm.html')
    # else:
    #     return redirect('error')