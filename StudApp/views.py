from django.shortcuts import render
from StudApp.models import StudentDB
from StudApp.serializers import Student_Serializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def StudentAPI(request, id=0):
    if request.method == "GET":
        x = StudentDB.objects.all()
        obj = Student_Serializer(x, many=True)
        return JsonResponse(obj.data, safe=False)
    elif request.method == "POST":
        x = JSONParser().parse(request)
        obj = Student_Serializer(data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Saved Successfully", safe=False)
        else:
            return JsonResponse("Data is Invalid !!!", safe=False)
    elif request.method == "PUT":
        x = JSONParser().parse(request)
        y = StudentDB.objects.get(StudID=x['StudID'])
        obj = Student_Serializer(y, data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated Successfully", safe=False)
        else:
            return JsonResponse("Data Update Failed", safe=False)
    elif request.method == "PATCH":
        x = JSONParser().parse(request)
        y = StudentDB.objects.get(StudID=x['StudID'])
        obj = Student_Serializer(y, data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated Successfully", safe=False)
        else:
            return JsonResponse("Data Update Failed", safe=False)
    elif request.method=="DELETE":
        x = StudentDB.objects.get(StudID=id)
        x.delete()
        return JsonResponse("Data Deleted", safe=False)





