import json
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import user,post
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import userSerializer, postSerializer
from django.db.models import Q


# Create your views here.
@csrf_exempt
def viewall(request):
    if request.method == 'POST':  
        blogList = post.objects.all()
        serializedData =postSerializer(blogList, many=True)
        return HttpResponse(json.dumps(serializedData.data))
    else:
        return HttpResponse(json.dumps({"status": "Failed", "message": "Invalid request method"}), status=405)
    
@csrf_exempt
#def viewalluser(request):
   #if request.method == 'POST':
        #user_list = user.objects.all()  # Replace 'YourUserModel' with the actual name of your model
        #serialized_data = userSerializer(user_list, many=True)  # Replace 'YourUserSerializer' with the actual name of your serializer
        #return HttpResponse(json.dumps(serialized_data.data), content_type='application/json')
   #else:
        #return HttpResponse(json.dumps({"status": "Failed", "message": "Invalid request method"}), status=405, content_type='application/json')


@csrf_exempt
def user(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)
        serializer_check = userSerializer(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed", "errors": serializer_check.errors}), status=406)
    else:
        return HttpResponse(json.dumps({"status": "Failed", "message": "Invalid request method"}), status=405)
    

@csrf_exempt
def add(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)
        serializer_check = postSerializer(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status": "Success"}))
        else:
            return HttpResponse(json.dumps({"status": "Failed", "errors": serializer_check.errors}), status=406)
    else:
        return HttpResponse(json.dumps({"status": "Failed", "message": "Invalid request method"}), status=405)


@csrf_exempt
def search(request):
    if request.method=="POST":
        received_data=json.loads(request.body)
        get_id=received_data["id"]
        data=list(post.objects.filter(Q(id__icontains=get_id)).values())
        return HttpResponse(json.dumps({"status":data}))


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        # Implement your delete logic here
        return HttpResponse(json.dumps({"status": "Failed", "message": "Not implemented"}), status=501)
    else:
        return HttpResponse(json.dumps({"status": "Failed", "message": "Invalid request method"}), status=405)
