from django.shortcuts import render,redirect
from .models import Parlor


def get_parlor_home(req):

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

        parlor=Parlor(parlor_name=parlor_name,parlor_description=parlor_desc,address=address,price=price)
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

        current_parlor.parlor_name=parlor_name
        current_parlor.parlor_description=parlor_desc
        current_parlor.address=address
        current_parlor.price=price

        current_parlor.save()

        return redirect('parlor_home')


def delete_parlor(req,ID):
    current_parlor=Parlor.objects.get(id=ID)
    current_parlor.delete()
    return redirect("parlor_home")