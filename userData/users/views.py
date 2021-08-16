from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Userinfo
from .serializers import userSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def listUserinfoAPI(request,*args, **kwargs):
    """
    REST API for fetching feeds at home page
    """
    Userinfos = Userinfo.objects.all()
    serialized_data = userSerializer(Userinfos, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def detailUserinfoAPI(request, uid, *args, **kwargs):
    """
    REST API for fetching feeds detail
    """
    try:
        obj = Userinfo.objects.get(id=uid)
        serialized_data = userSerializer(obj)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "NotFound"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def editUserinfoAPI(request, *args, **kwargs):
    """
    REST API for creating the Userinfo
    """
    serialized_obj = userSerializer(data=request.data)
    if serialized_obj.is_valid(raise_exception=True):
        Userinfo = serialized_obj.save()
        Userinfo = userSerializer(Userinfo)
        return Response({"Userinfo_obj": Userinfo.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "the form data is invalid"}, status=status.HTTP_400_BAD_REQUEST)

