from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import *
# Create your views here.


def about(request):
    return render(request,'about.html')

    
def contact(request):
    if request.method=='POST':
        try:
            if request.user.is_authenticated:
                if request.POST['name']!='' and request.POST['email']!='' and request.POST['subject']!='' and request.POST['msg']:
                    name=request.POST['name']
                    email=request.POST['email']
                    subject=request.POST['subject']
                    msg=request.POST['msg']
                    user=User.objects.get(id=request.user.id)
                    contact_msg(user=user,name=name,email=email,subject=subject,Msg=msg).save()
                    # cont.save()  
                    
                    msg1=(f'\n\n Name :  {name} \n Email :  {email} \n Message :  {msg}')
                    send_mail(subject,msg1,email,[settings.EMAIL_HOST_USER],fail_silently=False)
                    messages.success(request,'Your Message Send Successfully.')
                    return redirect(request.get_full_path())
                else:
                    return render(request,'contact-us.html',{'error':'All field are required !'})
            else:
                messages.warning(request,'Please login or register !')
                return redirect('login')

        except Exception as e:
            print(e)
    return render(request,'contact-us.html')