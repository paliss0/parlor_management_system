from django.shortcuts import render,redirect



def get_parlor_home(req):
    return render(req,'parlor_home.html')

def get_add_parlor(req):
    context={
        "page_title":"Add Parlor",
        "add_new_parlor":True
    }

    return render(req,'add_update_parlor.html',context=context)


def get_update_parlor(req,ID):
    context={
        "page_title":"Update Parlor"
    }

    return render(req,"add_update_parlor.html",context=context)

