import collections
from email.mime import message
import imp
from os import abort
from turtle import title
from unicodedata import category
from wsgiref.util import request_uri
from django import http
from django.shortcuts import redirect, render

from about.models import contact_msg
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from admin_dashboard.form import * 
# from login_register.models import *
from shop.models import *
from register.models import *
from django.contrib import messages as sms
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, JsonResponse
from admin_dashboard.templatetags.newfilter import *
# Create your views here.
import uuid




# def srch(request):
    
    # res={}
    # q= request.GET.get('q')
    # blg=blog_detail.objects.filter(blog_title__contains=q)
    # crs=course_detail.objects.filter(course_title__contains=q)
    # event=event_detail.objects.filter(event_title__contains=q)
    # prod=product_detail.objects.filter(product_title__contains=q)
    # inst=instructor.objects.filter(name__contains=q)
    # stud=student.objects.filter(name__contains=q)
    # if crs:
    #     paginator=Paginator(crs,6)
    #     page_no=request.GET.get('page')
    #     res['crs']=paginator.get_page(page_no)
    #     res['tot']=len(crs)
    #     return render(request,'event.html',res)
    # elif prod:
    #     paginator=Paginator(prod,6)
    #     page_no=request.GET.get('page')
    #     res['product']=paginator.get_page(page_no)
    #     res['tot']=len(prod)
    #     return render(request,'event.html',res)
    # elif blg:
    #     paginator=Paginator(blg,6)
    #     page_no=request.GET.get('page')
    #     res['blogs']=paginator.get_page(page_no)
    #     res['tot']=len(blg)
    #     return render(request,'event.html',res)
    # elif event:
    #     paginator=Paginator(event,6)
    #     page_no=request.GET.get('page')
    #     res['event']=paginator.get_page(page_no)
    #     res['tot']=len(event)
    #     return render(request,'event.html',res)
    # elif inst:
    #     paginator=Paginator(inst,6)
    #     page_no=request.GET.get('page')
    #     res['inst']=paginator.get_page(page_no)
    #     res['tot']=len(inst)
    #     return render(request,'event.html',res)
    # elif stud:
    #     paginator=Paginator(stud,6)
    #     page_no=request.GET.get('page')
    #     res['stud']=paginator.get_page(page_no)
    #     res['tot']=len(stud)
    #     return render(request,'event.html',res)

    # return redirect('404')

def ad_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        li=[]
        res['usr']=User.objects.filter(is_superuser=False)
       
        # res['totl_stud']=userType.objects.filter(type='2').count()
        # res['totl_inst']=userType.objects.filter(type='1').count()
        res['totl_product']=productDetail.objects.all().count()
        # res['totl_crs']=course_detail.objects.all().count()
        # res['inst']=instructor.objects.all().order_by('-id')
        # res['stud']=student.objects.all().order_by('-id')
        
        # crs=course_detail.objects.values('course_instructor__name').all()
        # print(crs,'ll')
        # ret=collections.defaultdict(int)
        # li=[]
        # for c in instructor.objects.all():
        #     inst_crs=course_detail.objects.filter(course_instructor=c).count()     
        #     li.append({'id':c.id,'crs_cunt':inst_crs})
        # res['crs_count']=li
        return render(request,'admin-index.html',res)
    else:
        return redirect('ad_login')
def payments(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
    # crs_order=courses_purchase_order.objects.values('user','amount')
    # ret=collections.defaultdict(int)
    # for c in crs_order:
    #     ret[c['user']]+=int(c['amount'])
    #     crs=[{'usr':us,'amount':am} for us,am in ret.items()]
    # prod_order=products_purchase_order.objects.values('user','amount')
    # ret=collections.defaultdict(int)
    # for p in prod_order:
    #     ret[p['user']]+=int(p['amount'])
    #     prod=[{'usr':us,'amount':am} for us,am in ret.items()]
    # ret=collections.defaultdict(int)
    # for u in crs+prod:
    #     ret[u['usr']]+=int(u['amount'])
    #     rs=[{'usr':us,'amount':am} for us,am in ret.items()]
    # li=[]
    # for r in rs:
    #     inst=instructor.objects.filter(user__id=r['usr'])
    #     if inst:
    #         li.append([inst,r])
    #     stud=student.objects.filter(user__id=r['usr'])
    #     if stud:
    #         li.append([stud,r])
    # res['usrs']=li
        # crs=courses_purchase_order.objects.all()
        # prod=products_purchase_order.objects.all()
        # from itertools import chain
        # pymnt_all = list(chain(crs,prod))
        # tot=0
        # for i in pymnt_all:
        #     tot+=i.amount
        #     res['amnt']={'amount':tot}
        # res['crs']=crs.count()
        # res['prod']=prod.count()
        # res['inst']=instructor.objects.all()
        # res['stud']=student.objects.all()
        # paginator=Paginator(pymnt_all,10)
        # page_no=request.GET.get('page')
        # res['pymnts_all']=paginator.get_page(page_no)
        # res['tot']=len(pymnt_all)
        # res['typ']=userType.objects.all()
        # trans=PaytmTransaction.objects.all()
        # paginator=Paginator(trans,10)
        # page_no=request.GET.get('page')
        # res['trans']=paginator.get_page(page_no)
        return render(request,'payment-trans.html',res)
    else:
        return redirect('ad_login')
# def ad_register(request):

#         if request.method == "POST":
#                     name = request.POST['name']
#                     email = request.POST['email']
#                     password = request.POST['password']
#                     confirm=request.POST['confirm']
#                     usermail = User.objects.filter(email=email)
#                     if len(usermail) !=1 :
#                             if confirm==password: 
#                                 user =User.objects.create_superuser(username=name, email=email, password=password)
#                                 user.save()
#                                 frgpwd=frgt_pwd(user=user,frg_token=str(uuid.uuid4()))
#                                 frgpwd.save()
#                                 pro=admin_profile(user=user,email=email,name=name)
#                                 pro.save()
#                                 sms.success(request,'Regiter Successfully.')
#                                 return redirect('ad_login')
#         return render(request,'create-account.html')
def ad_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('ad_dash')
    else:
        res={}
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            USER = authenticate(request,username=username, password=password)
            if USER is not None:
                login(request, USER)
                if request.user.is_superuser:
                    sms.success(request,'Login Success.')
                    return redirect('ad_dash')
                else:
                    
                    sms.error(request,'wrong username or password!')
                    return redirect('ad_login')
            
            else:
                sms.error(request,'Invalid Username or Password!')
                return redirect('ad_login')
                
        return render(request,'logn.html',res)
def ad_logout(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            logout(request)
            sms.success(request,'Logout Successfully.')
            return redirect('ad_login')
        except Exception as e:
            sms.warning(request,'something went wrong !')
            return redirect('ad_login')
    else:
         return redirect('ad_login')
def ad_forgot_pwd(request):
    if request.user.is_authenticated!=True and request.user.is_superuser!=True:
        
        if request.method=='POST':
            try:
                email=request.POST['email']
                useremail=User.objects.get(email=email)
                frgtoken=frgt_pwd.objects.get(user=useremail)
                ftoken=frgtoken.frg_token
                emails=useremail.email   
                mail_msg=f'Your reset password link is http://127.0.0.1:8000/dashboard/password-change/{ftoken}.'
                # mail_msg=f'Set Password \n Your reset password link is https://cyberacdamy.herokuapp.com/dashboard/password-change/{ftoken}.'
                send_mail('For reset password', mail_msg,settings.EMAIL_HOST_USER, [emails],fail_silently=False)
                sms.success(request, "Mail Send Successfully.\n Please Check Your Email.")
                return redirect('ad_forgot_pwd')
            except Exception as e:
                sms.error(request,'Invalid Email!')
        return render(request,'admin-forgot-password.html')

    else:
        return redirect('error')  
def pwd_reset_change(request,id):
    if request.user.is_authenticated!=True and request.user.is_superuser!= True:
        if request.method=='POST':
            try:
                pass1=request.POST['pass1']
                confirm=request.POST['pass2']
                if pass1==confirm:
                    frgpwd=frgt_pwd.objects.get(frg_token=id)
                    user=User.objects.get(username=frgpwd)
                    user.set_password(pass1)
                    user.save()
                    sms.success(request, "Password Change Successfully.\n +Please login. ")
                    return redirect('ad_login')
                else:
                    sms.error(request,'Password Not Match.Enter Same Password.')
            except Exception as e:
                print(e)
        return render(request,'pwd_change.html')
    else:
        return redirect('error')

def ad_profile(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        nxt=request.get_full_path()
        res['profile']=admin_profile.objects.filter(user=User.objects.get(id=request.user.id))
        if request.method=='POST':
            
            if request.POST.get('usr')!=None:
                email=request.POST['email']
                name=request.POST['name']
                img=request.FILES['img']
                dob=request.POST['dob']
                address=request.POST['address']
                about=request.POST['about'] 
                phone=request.POST['phone']
                
                pro= admin_profile.objects.filter(user=User.objects.get(id=request.POST['usr']))
                if len(pro)>0:
                    ob=pro[0]
                    ob.user=User.objects.get(id=request.user.id)
                    if len(name)>0:
                        ob.name=name
                    if len(img)>0:
                        ob.img=img
                    if len(email)>0:
                        ob.email=email
                    if len(dob)>0:
                        ob.dob=dob
                    if len(phone)>0:
                        ob.mobile=phone
                    if len(about)>0:
                        ob.about=about
                    if len(address)>0:
                        ob.address=address
                    ob.save()
                    sms.success(request,'Profile Updated.')
                    return redirect(nxt)
                else:
                    try:
                        admin_profile(user=User.objects.get(id=request.user.id),name=name,img=img,email=email,dob=dob
                        ,mobile=phone,about=about,address=address).save()
                        sms.success(request,'Profile Updated.')
                        return redirect(nxt)
                    except Exception as e:
                        res['error']='All Field Required !'
                        return render(request,'profiles.html',res)
            
            elif request.POST.get('us')!=None:
                logo=request.POST['logo']
                favicon=request.POST['fav']
                title=request.POST['title']
                if favicon!='' and title!='' and logo!='':   
                    setting.objects.all().delete()
                    setting(title=title,logo=logo,favicon=favicon).save()
                    sms.success(request,'Profile Setting Updated.')
                    return redirect(nxt)
                elif favicon!='':
                    sett=setting.objects.all()
                    if len(sett)>0:
                        ob=sett[0]
                        ob.favicon=favicon
                        ob.save()
                        sms.success(request,'Profile Setting Updated.')
                        return redirect(nxt)
                elif logo!='':
                    sett=setting.objects.all()
                    if len(sett)>0:
                        ob=sett[0]
                        ob.logo=logo
                        ob.save()
                        sms.success(request,'Profile Setting Updated.')
                        return redirect(nxt)
                elif title!='':
                    sett=setting.objects.all()
                    if len(sett)>0:
                        ob=sett[0]
                        ob.title=title
                        ob.save()
                        sms.success(request,'Profile Setting Updated.')
                        return redirect(nxt)
                    

            elif request.POST.get('uss')!=None:
                print(request.POST.get('uss'),'[[')
                old = request.POST['old']
                new = request.POST['new']
                confirm = request.POST['confirm']
                user = User.objects.get(id=request.user.id)
                mail=user.email
                check=user.check_password(old)
                if confirm==new:
                    if check==True:
                        user.set_password(new)
                        user.save()
                        user=User.objects.get(email=mail)
                        login(request,user)
                        sms.success(request, "Password Updated")
                        return redirect(nxt)
                    else:
                        sms.error(request, "Incorrect Old Password")
                        return redirect(nxt)
                else:
                    sms.error(request,'New And Confirm Password Not Match.')
        

        return render(request,'profiles.html',res)
    else:
        return redirect('ad_login')
def error404(request):
    return render(request,'error.html')


def ad_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['products']=productDetail.objects.all()
        paginator=Paginator(res['products'],6)
        page_no=request.GET.get('page')
        res['product']=paginator.get_page(page_no)
        res['tot']=len(res['products'])
        res['cat']=productCategory.objects.all()
        nxt=request.get_full_path()
        if request.method=='POST':
            if request.POST.get('prid')!=None: # for delete
                prid=request.POST['prid']
                prod=productDetail.objects.filter(id=prid)
                prod.delete()
                sms.success(request,'Product Deleted SuccessFully.')
                return redirect(nxt)
            elif request.POST.get('pid')!=None: # for edit
                name=request.POST['name']
                desc=request.POST['desc'] 
                about=request.POST['about'] 
                img=request.POST['img']
                quntity=request.POST['qunt']
                
                pr= productDetail.objects.filter(id=request.POST['pid'])
               
                if len(pr)>0:
                    ob=pr[0]
                    if len(name)>0:
                        ob.name=name
                    if len(img)>0:
                        ob.img=img
                    if len(desc)>0:
                        ob.long_description=desc
                    if len(quntity)>0:
                        ob.quntity=quntity
                    if len(about)>0:
                        ob.about=about
                    
                    ob.save()
                    sms.success(request,'Product Updated.')
                    return redirect(nxt)    
           
        return render(request,'product.html',res)
    else:
        return redirect('ad_login')
def add_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['thick']=productThickness.objects.all()
        res['mate']=productMaterial.objects.all()
        res['size']=productSize.objects.all()
        res['color']=productStyle.objects.all()
        res['cat']=productCategory.objects.all()
        res['uses']=productUses.objects.all()
        if request.method=='POST'  :
                
                name=request.POST['name']
                desc=request.POST['desc'] 
                about=request.POST['about'] 
                img=request.POST['img']
                quntity=request.POST['qunt']

                mate=request.POST.getlist('mate')
                use=request.POST.getlist('use') 
                try:
                
                        prod= productDetail(name=name,img=img,quntity=quntity,about=about,long_description=desc)
                        prod.save()
                        for i in mate:
                            prod.material.add(productMaterial.objects.get(id=i))
                        for i in use:
                            prod.uses.add(productUses.objects.get(id=i))

                        sms.success(request,'Product Added.')
                        return redirect('ad_product')
                except Exception as p:
                    sms.warning(request,'All Field Are Required !')
                    return redirect('add_product')
    
        return render(request,'add-product.html',res)
    else:
        return redirect('ad_login')



def pric(request):

    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['prod']=productDetail.objects.all()
        res['price']=prices.objects.all()
       
        res['thick']=productThickness.objects.all()
        res['mate']=productMaterial.objects.all()
        res['size']=productSize.objects.all()
        res['color']=productStyle.objects.all()
        res['cat']=productCategory.objects.all()
        res['uses']=productUses.objects.all()
        if request.method=='POST'  :
                    
                    if request.POST.get('usesid')!=None:
                        pri=prices.objects.filter(product=productDetail.objects.get(id=request.POST.get('usesid'))).delete() 
                        sms.success(request,'Price Deleted.')
                        return redirect('price')
                    name=request.POST['name']
                    base=request.POST['base']
                    trans=request.POST['trans'] 
                    gst=request.POST['gst']
                    dis=request.POST['dis']

                    size=request.POST.getlist('size')
                    cat=request.POST['cat']
                    thick=request.POST.getlist('thick')
                    color=request.POST.getlist('color')
                    print(cat,'ooo',trans)
                    pri=prices.objects.filter(product=productDetail.objects.get(id=name))
                # try:
                    if int(dis)<100:
                        if len(pri)==0:
                            prod= prices(product=productDetail.objects.get(id=name),discount=dis,price_base=base,transports=trans,gst=gst,
                            category=productCategory.objects.get(id=cat))
                            prod.save()
                            for i in size:
                                prod.size.add(productSize.objects.get(id=i))
                            for i in color:
                                prod.color.add(productStyle.objects.get(id=i))
                            for i in thick:
                                prod.thickness.add(productThickness.objects.get(id=i))
                            
                            sms.success(request,'Price Added.')
                            return redirect('price')
                        elif len(pri)>0:
                            ob=pri[0]



                            if len(size)>0:

                                for i in size:
                                    ob.size.add(productSize.objects.get(id=i))
                            if len(cat)>0:
                                for i in color:
                                    ob.color.add(productStyle.objects.get(id=i))
                            if len(thick)>0:
                                for i in thick:
                                    ob.thickness.add(productThickness.objects.get(id=i))
                            
                            if len(name)>0:
                                ob.product=productDetail.objects.get(id=name)
                            if len(dis)>0:
                                ob.discount=dis
                            if  cat!=None and cat!=0:
                                ct=productCategory.objects.filter(id=cat)
                                if ct:
                                    ob.category=productCategory.objects.get(id=cat)
                            if len(base)>0:
                                ob.price_base=base
                            if len(trans)>0:
                                ob.transports=trans
                            if len(gst)>0 :
                                ob.gst=gst
                            ob.save()  
                            sms.success(request,'Price Edited.')
                            return redirect('price')
                    else:
                        sms.warning(request,'Discount should be under 100%.')
                        return redirect('price')
                # except Exception as p:
                #     sms.warning(request,'All Field Are Required !')
                #     return redirect('price')
    
        return render(request,'price.html',res)
    else:
        return redirect('ad_login')




def  prod_size(request):
    if request.user.is_authenticated and request.user.is_superuser:
   
        res={}
        nxt=request.get_full_path()
        res['size']=productSize.objects.all()
        if request.method=='POST':
                if request.POST.get('mesu')!=None:#for size add
                    mesu=request.POST['mesu']
                    len=request.POST['len'] 
                    width=request.POST['width']
                    hei=request.POST['hei']
                    min=request.POST['min'] 
                    max=request.POST['max'] 
                    productSize(width=width,lenght=len,max=max,min=min,height=hei,meassuement=mesu).save()
                    sms.success(request,'Size Added.')
                    return redirect(nxt)
                elif request.POST.get('sizeid')!='':#for delete size
                    size=request.POST['sizeid'] 
                    productSize(id=size).delete()
                    sms.success(request,'Size Deleted.')
                    return redirect(nxt)
                
        return render(request,'prod-size.html',res)
    else:
        return redirect('ad_login')



def  prod_uses(request):
    if request.user.is_authenticated and request.user.is_superuser:
   
        res={}
        nxt=request.get_full_path()
        res['uses']=productUses.objects.all()

        if request.method=='POST':
                print( request.POST.get('usesid') ,'//////', request.POST.get('eid'))
                if request.POST.get('uses')!=None:#for uses add
                    uses=request.POST['uses'] 
                    productUses(uses=uses).save()
                    sms.success(request,'Uses Added.')
                    return redirect(nxt)
                elif request.POST.get('usesid')!=None:#for delete uses
                    uses=request.POST['usesid'] 
                    productUses(id=uses).delete()
                    sms.success(request,'Uses Deleted.')
                    return redirect(nxt)
                elif request.POST.get('eid')!='':#for edit uses
                    uses=request.POST['eid'] 
                    use=request.POST['use'] 
                    pro=productUses.objects.get(id=uses)
                    pro.uses=use
                    pro.save()
                    sms.success(request,'Uses Edited.')
                    return redirect(nxt)
                
        return render(request,'prod-uses.html',res)
    else:
        return redirect('ad_login')


def  thick_mtrial(request):
    if request.user.is_authenticated and request.user.is_superuser:
   
        res={}
        nxt=request.get_full_path()
        res['mate']=productMaterial.objects.all()
        res['thick']=productThickness.objects.all()

        print( request.POST.get('thickid'),'////', request.POST.get('mateid'))
        if request.method=='POST':
            if request.POST.get('thick')!=None:#for add thick
                    thick=request.POST['thick']
                    productThickness(thickness=thick).save()
                    sms.success(request,'Thickness Added.')
                    return redirect(nxt)
            elif request.POST.get('mate')!=None:#for add material
                    mate=request.POST['mate'] 
                    productMaterial(material=mate).save()
                    sms.success(request,'Material Added.')
                    return redirect(nxt)
            elif request.POST.get('thickid')!='':#for delete thick
                    thick=request.POST['thickid']
                    productThickness(id=thick).delete()
                    sms.success(request,'Thickness Deleted.')
                    return redirect(nxt)
        
            elif request.POST.get('mateid')!='':#for delete material
                    mate=request.POST['mateid'] 
                    productMaterial(id=mate).delete()
                    sms.success(request,'Material Deleted.')
                    return redirect(nxt)
                
        return render(request,'thick-mate-table.html',res)
    else:
        return redirect('ad_login')
def  style_cate(request):
    if request.user.is_authenticated and request.user.is_superuser:
   
        res={}
        nxt=request.get_full_path()
        res['style']=productStyle.objects.all()
        res['cate']=productCategory.objects.all()
        print(request.POST.get('style'),'sss',request.POST.get('cateid'),'uu',request.POST.get('cate'),'ll',request.POST.get('styleid'))
        if request.method=='POST':
            if request.POST.get('style')!=None:#for add style
                    style=request.POST['style']
                    productStyle(color=style).save()
                    sms.success(request,'Style Added.')
                    return redirect(nxt)
            elif request.POST.get('cate')!=None:#for add category
                    cate=request.POST['cate'] 
                    productCategory(category=cate).save()
                    sms.success(request,'Category Added.')
                    return redirect(nxt)
            elif request.POST.get('styleid')!='':#for delete style
                    style=request.POST['styleid']
                    productStyle(id=style).delete()
                    sms.success(request,'Style Deleted.')
                    return redirect(nxt)
            
            elif request.POST.get('cateid')!='':#for delete category
                    cate=request.POST['cateid'] 
                    productCategory(id=cate).delete()
                    sms.success(request,'Category Deleted.')
                    return redirect(nxt)
                
        return render(request,'style-cat.html',res)

    else:
        return redirect('ad_login')


def  prod_coupn(request):
    if request.user.is_authenticated and request.user.is_superuser:
   
        res={}
        nxt=request.get_full_path()
        res['cop']=coupons.objects.all()
    
        if request.method=='POST':
            
                if request.POST.get('name')!=None:#for uses add
                    name=request.POST['name'] 
                    dis=request.POST['dis'] 
                    qunt=request.POST['qunt'] 
                    valid=request.POST['valid'] 
                    min=request.POST['min'] 
                    code=request.POST['code'] 
                    if int(dis)<100:
                        coupons(coupan_code=code,coupan_name=name,Coupon_expire_date=valid,quantity=int(qunt)
                        ,minimum_order_value=min,discount=int(dis)).save()
                        sms.success(request,'Coupon Added.')
                        return redirect(nxt)
                    else:
                        sms.warning(request,'Discount should be under 100%. ')
                        return redirect(nxt)
                   
                elif request.POST.get('coid')!=None:#for delete copn
                    uses=request.POST['coid'] 
                    coupons(id=uses).delete()
                    sms.success(request,'Coupon Deleted.')
                    return redirect(nxt)
                elif request.POST.get('copid')!='':#for edit copn
                    copid=request.POST['copid'] 
                    qunt=request.POST['qunt'] 
                    value=request.POST['value']
                    copname=request.POST['copname'] 
                    dis=request.POST['dis']
                    date=request.POST['date'] 
                    code=request.POST['code'] 
                    
                    pro=coupons.objects.get(id=copid)
                    if len(code)>0:
                        pro.coupan_code=code
                    if len(date)>0:
                        pro.Coupon_expire_date=date
                    if len(qunt)>0:
                        pro.quantity=int(qunt)
                    if len(value)>0:
                        pro.minimum_order_value=value
                    if len(dis)>0 and int(dis)<100:
                        pro.discount=int(dis)
                    else:
                        sms.warning(request,'Discount should be under 100%. ')
                        return redirect(nxt)
                    if len(copname)>0:
                        pro.coupan_name=copname
                    pro.save()
                    sms.success(request,'Coupon Edited.')
                    return redirect(nxt)
                
        return render(request,'prod-coupon.html',res)
    else:
        return redirect('ad_login')



def cont(request):
    if request.user.is_authenticated and request.user.is_superuser:
        res={}
        res['cont']=contact_msg.objects.all()
        return render(request,'contact-msg.html',res)
    else:
        return redirect('ad_login')



