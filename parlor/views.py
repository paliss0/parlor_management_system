from django.shortcuts import render,redirect
from .models import Parlor
from django.core.files.storage import FileSystemStorage


def get_parlor_home(req):

    if not req.user.is_authenticated:
        return redirect('login')
        
    all_parlor=Parlor.objects.all()

    if 'search_query' in req.GET:
        search_query=req.GET['search_query']
        if search_query == "":
            all_parlor=Parlor.objects.all()
        else:
            all_parlor=Parlor.objects.filter(parlor_name=search_query)
    
    context={
        "parlors":all_parlor
    }
    return render(req,'parlor_home.html',context=context)

def get_add_parlor(req):
    if req.method=="GET":
        context={
            "page_title":"Add Parlor"
        }

        return render(req,'add_update_parlor.html',context=context)
    else:
        parlor_name=req.POST['parlor_name']
        parlor_desc=req.POST['parlor_description']
        address=req.POST['address']
        price=req.POST['price']

        parlor_logo=req.FILES["parlor_logo"]

        fs=FileSystemStorage()
        filename=fs.save(parlor_logo.name,parlor_logo)
        url=fs.url(filename)
        
        parlor=Parlor(parlor_logo=url,parlor_name=parlor_name,parlor_description=parlor_desc,address=address,price=price)
        parlor.save()

        return redirect('parlor_home')





def get_update_parlor(req,ID):
    current_parlor=Parlor.objects.get(id=ID)

    if req.method=="GET":
        context={
            "page_title":"Update Parlor",
            "update_parlor":True,
            "parlor":current_parlor

        }

        return render(req,"add_update_parlor.html",context=context)
    else:

        parlor_name=req.POST['parlor_name']
        parlor_desc=req.POST['parlor_description']
        address=req.POST['address']
        price=req.POST['price']

        parlor_logo=req.FILES["parlor_logo"]

        fs=FileSystemStorage()
        filename=fs.save(parlor_logo.name,parlor_logo)
        url=fs.url(filename)


        current_parlor.parlor_name=parlor_name
        current_parlor.parlor_logo=url
        current_parlor.parlor_description=parlor_desc
        current_parlor.address=address
        current_parlor.price=price

        current_parlor.save()

        return redirect('parlor_home')


def delete_parlor(req,ID):
    current_parlor=Parlor.objects.get(id=ID)
    current_parlor.delete()
    return redirect("parlor_home")