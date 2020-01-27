from django.shortcuts import render,redirect
from .models import Parlor


def get_parlor_home(req):
    return render(req,'parlor_home.html')

def get_add_parlor(req):
    if req.method=="GET":
        context={
            "page_title":"Add Parlor",
            "add_new_parlor":True
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
    context={
        "page_title":"Update Parlor"
    }

    return render(req,"add_update_parlor.html",context=context)

