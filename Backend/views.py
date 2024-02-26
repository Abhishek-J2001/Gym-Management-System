from django.shortcuts import render,redirect
from Backend.models import Category,ManagePackage,AddPackage
from Frontend.models import contact,payment,RegisterDB,blog
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def managepackage(request):
    return render(request,"managecategory.html")

def savedata(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        des = req.POST.get('description')
        obj = Category(categoryname=cn, description=des)
        obj.save()
        messages.success(req,"Category Saved Successfully..!")
        return redirect(managepackage)

def catdisplay(request):
    data = Category.objects.all()
    return render(request, "CategoryDisplay.html", {'data': data})
    messages.success(request, "Category Edited Successfully..!")

def editpage(req,dataid):
    data = Category.objects.get(id=dataid)
    return render(req,"EditCategory.html", {'data': data})

def deletecat(request, dataid):
    cat = Category.objects.filter(id=dataid)
    cat.delete()
    messages.success(request, "Category Deleted Successfully..!")
    return redirect(catdisplay)

def updatedata(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        des = request.POST.get('description')
        Category.objects.filter(id=dataid).update(categoryname=cn, description=des)
        messages.success(request, "Category Edited Successfully..!")
        return redirect(catdisplay)

def managepackagetype(request):
    category = Category.objects.all()
    return render(request,"ManagePackageType.html" ,{'category':category})

def savedat(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        img = request.FILES.get('image')
        obj = ManagePackage(categoryname=cn, packagename=pn, Packageimage=img)
        obj.save()
        messages.success(request,"Package Added Successfully..!")
        return redirect(managepackagetype)

def packdisplay(request):
    data = ManagePackage.objects.all()
    return render(request, "ManagePackageDisplay.html", {'data': data})
    messages.success(request, "Category Edited Successfully..!")

def editpack(request, dataid):
        data = ManagePackage.objects.get(id=dataid)
        cat = Category.objects.all()
        return render(request, "EditPackgeType.html", {'data': data, 'cat': cat})

def deletepack(request, dataid):
        pro = ManagePackage.objects.filter(id=dataid)
        pro.delete()
        return redirect(packdisplay)

def updatepack(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ManagePackage.objects.get(id=dataid).Packageimage
        ManagePackage.objects.filter(id=dataid).update(categoryname=cn,packagename=pn, Packageimage=file)
        messages.success(request, "Package Name Edited Successfully..!")
        return redirect(packdisplay)

def addpackage(request):
    category = Category.objects.all()
    package = ManagePackage.objects.all()
    return render(request,"AddPackage.html",{'category':category,'package':package})

def addpack(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        tl = request.POST.get('titlename')
        du = request.POST.get('time')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        obj = AddPackage(categoryname=cn, packagename=pn,title=tl, duraction=du, price=pr, description=des)
        obj.save()
        messages.success(request,"Package Saved Successfully..!")
        return redirect(addpackage)

def addpackdisplay(request):
    data = AddPackage.objects.all()
    return render(request, "PackageDisplay.html", {'data': data})
    messages.success(request, "Category Edited Successfully..!")

def editpackage(request, dataid):
        data = AddPackage.objects.get(id=dataid)
        cat = Category.objects.all()
        pack = ManagePackage.objects.all()
        return render(request, "EditPackage.html", {'data': data,'cat':cat,'pack':pack})


def deletepackage(request, dataid):
    pro = AddPackage.objects.filter(id=dataid)
    pro.delete()
    return redirect(addpackdisplay)

def updatepackage(request,dataid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        tl = request.POST.get('titlename')
        du = request.POST.get('time')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        AddPackage.objects.filter(id=dataid).update(categoryname=cn, packagename=pn, title=tl, duraction=du, price=pr, description=des)
        messages.success(request, "Package Name Edited Successfully..!")
        return redirect(addpackdisplay)



def admin_login(req):
    return render(req,"AdminLogin.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def displaycontact(request):
    data = contact.objects.all()
    return render(request,"Contact_Details.html", {'data':data})

def deletecon(request, dataid):
    pro = contact.objects.filter(id=dataid)
    pro.delete()
    messages.success(request, "Comment Deleted Successfully..!")
    return redirect(displaycontact)

def displaypayment(request):
    data = payment.objects.all()
    return render(request,"paymentdetails.html", {'data':data})

def displayblog(request):
    data = blog.objects.all()
    return render(request,"displayblog.html", {'data':data})

def deleteblog(request, dataid):
    pro = blog.objects.filter(id=dataid)
    pro.delete()
    messages.success(request, "Comment Deleted Successfully..!")
    return redirect(displayblog)

def displayreg(request):
    data = RegisterDB.objects.all()
    return render(request,"Registeredusers.html", {'data':data})
