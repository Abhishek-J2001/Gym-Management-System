from django.shortcuts import render,redirect
from Backend.models import AddPackage
from Frontend.models import contact,payment,blog,RegisterDB
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def homepage(request):
    cat = AddPackage.objects.all()
    return render(request,"Home.html",{'cat':cat})

def aboutpage(request):
    return render(request,"About.html")

def contactpage(request):
    return render(request,"contactpage.html")

def contactdata(req):
    if req.method == "POST":
        cn = req.POST.get('name')
        ce = req.POST.get('email')
        cm = req.POST.get('mobile')
        com = req.POST.get('comment')
        obj = contact(Name=cn, Email=ce, mobile=cm, comment=com)
        obj.save()
        messages.success(req,"Comment Sended Successfully..!")
        return redirect(contactpage)

def classpage(request):
    return render(request,"class_details.html")

def classtimepage(request):
    return render(request,"classtimetable.html")

def servicepage(request):
    cat = AddPackage.objects.all()
    return render(request,"service.html",{'cat':cat})

def teampage(request):
    return render(request,"team.html")

def paymentpage(request):
    cat = AddPackage.objects.all()
    return render(request,"payment.html",{'cat':cat})

def paymentdata(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        ad = request.POST.get('address')
        st = request.POST.get('state')
        pin = request.POST.get('pincode')
        cn = request.POST.get('cname')
        cnum = request.POST.get('cnum')
        expm = request.POST.get('expm')
        expy = request.POST.get('expy')
        cvv = request.POST.get('cvv')
        pr = request.POST.get('price')
        obj = payment(Name=n, Email=e, Address=ad, State=st, Pincode=pin, NameOnCard=cn, CardNumber=cnum, ExpMonth=expm, ExpYear=expy, CVV=cvv, price=pr)
        obj.save()
        return redirect(homepage)



def blogpage(request):
    return render(request,"Blogs.html")

def blogdata(req):
    if req.method == "POST":
        n = req.POST.get('name')
        e = req.POST.get('email')
        m = req.POST.get('mobile')
        com = req.POST.get('comment')
        obj = blog(Name=n, Email=e, mobile=m, comment=com)
        obj.save()
        messages.success(req,"Comment Sended Successfully..!")
        return redirect(blogpage)

def regpage(request):
    return render(request,"Register.html")

def savereg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        img = request.FILES.get('image')
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = RegisterDB(Name=na, Email=em, Image=img, Username=un, Password=pwd)
        obj.save()
        return redirect(login_page)

def edit_page(request):
    data = RegisterDB.objects.get(id=request.session['UserId'])
    return render(request,"EditProfile.html", {'data': data})

def updateprofile(request, dataid):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = RegisterDB.objects.get(id=dataid).Image
        RegisterDB.objects.filter(id=dataid).update(Name=n, Email=e, Username=un, Password=pwd, Image=file)
        messages.success(request, "Profile Edited Successfully..!")
        return redirect(homepage)

def login_page(request):
    return render(request,"login.html")


def user_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegisterDB.objects.filter(Username=un, Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            user = RegisterDB.objects.get(Username=un, Password=pwd)
            request.session['UserId'] = user.id
            return redirect(homepage)
        else:
            return redirect(login_page)
    else:
        return redirect(login_page)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(login_page)

def profile_page(request):
    data = RegisterDB.objects.filter(id=request.session['UserId'])
    return render(request,"MyProfile.html",{'data':data})
