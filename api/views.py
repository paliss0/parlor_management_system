from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from parlor.models import Parlor

def view_get_post_parlor(req):

    if req.method=="GET":
        pass

    elif req.method=="POST":
        pass


def view_getByID_updateByID_deleteByID(req,ID):
    current_parlor=Parlor.objects.get(id=ID)
    if req.method=="GET":
        return JsonResponse({
            "parlor":{
                "id":current_parlor.id,
                "parlor_name":current_parlor.palor_name,
                "parlor_description":current_parlor.parlor_description,
                "address":current_parlor.address,
                "price":current_parlor.price
            }
        })

    elif req.method=="PUT":
        pass

    elif req.method=="DELETE":
        current_parlor.delete()

        return JsonResponse({
            "message":"Item Deleted",
            "item":{
                "id":current_parlor.id,
                "parlor_name":current_parlor.palor_name,
                "parlor_description":current_parlor.parlor_description,
                "address":current_parlor.address,
                "price":current_parlor.price
            }
        })