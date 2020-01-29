from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from parlor.models import Parlor
import json

@csrf_exempt
def view_get_post_parlor(req):

    if req.method=="GET":
        db_parlors=Parlor.objects.all()
        all_parlors=list(db_parlors.values())
        print(all_parlors)
        return JsonResponse({
            "parlors":all_parlors
        })

    elif req.method=="POST":
        body=json.loads(req.body)
        current_parlor=Parlor.objects.create(parlor_name=body['parlor_name'],parlor_description=body['parlor_description'],address=body['address'],price=body['price'])
        current_parlor.save()
        return JsonResponse({
            "message":"Parlor Created",
            "parlor":{
                "id":current_parlor.id,
                "parlor_name":current_parlor.parlor_name,
                "parlor_description":current_parlor.parlor_description,
                "address":current_parlor.address,
                "price":current_parlor.price
            }
        })

@csrf_exempt
def view_getByID_updateByID_deleteByID(req,ID):
    current_parlor=Parlor.objects.get(id=ID)
    if req.method=="GET":
        return JsonResponse({
            "parlor":{
                "id":current_parlor.id,
                "parlor_name":current_parlor.parlor_name,
                "parlor_description":current_parlor.parlor_description,
                "address":current_parlor.address,
                "price":current_parlor.price
            }
        })

    elif req.method=="PUT":
        body=json.loads(req.body)
        current_parlor.parlor_name=body['parlor_name']
        current_parlor.parlor_description=body['parlor_description']
        current_parlor.address=body['address']
        current_parlor.price=body['price']

        current_parlor.save()

        return JsonResponse({
            "message":"Updated Parlor",
            "parlor":{
                "id":current_parlor.id,
                "parlor_name":current_parlor.parlor_name,
                "parlor_description":current_parlor.parlor_description,
                "address":current_parlor.address,
                "price":current_parlor.price
            }
        })

    elif req.method=="DELETE":
        current_parlor.delete()

        return JsonResponse({
            "message":"Parlor Deleted",
            "item":{
                "id":current_parlor.id,
                "parlor_name":current_parlor.parlor_name,
                "parlor_description":current_parlor.parlor_description,
                "address":current_parlor.address,
                "price":current_parlor.price
            }
        })