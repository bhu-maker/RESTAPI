from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  .import models
from .serializers import corpseri
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET','POST'])
def listing(request):
    if request.method=='GET':
        modvar=models.corporates.objects.all()
        servar=corpseri(modvar,many=True)
        return Response(servar.data)
    elif request.method=='POST'    :
        servar=corpseri(data=request.data)
        if servar.is_valid():
            servar.save()
            return Response(servar.data,status=status.HTTP_201_CREATED)
        return Response(servar.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])        
def apilisting(request):
       servar=corpseri(data=request.data)
       if servar.is_valid():
           servar.save()
           return Response(servar.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])           
def apigetting(request):
    modvar=models.corporates.objects.all()
    servar=corpseri(modvar,many=True)
    return Response(servar.data)

@api_view(['GET'])    
def apireading(request,para):
    modvar=models.corporates.objects.get(org=para)
    servar=corpseri(modvar)
    return Response(servar.data,status=status.HTTP_200_OK)

@api_view(['GET'])    
def apireadingbyid(request,para):
    modvar=models.corporates.objects.get(id=para)
    servar=corpseri(modvar)
    return Response(servar.data,status=status.HTTP_200_OK)    

@api_view(['POST'])    
def putting(request,pk):
    modvar=models.corporates.objects.get(id=pk)
    servar=corpseri(instance=modvar,data=request.data)
    if servar.is_valid():
        servar.save()
        return Response(servar.data)
    return Response(servar.error,status=status.HTTP_404_NOT_FOUND)  

@api_view(['DELETE'])      
def deleting(request,pk):
    modvar=models.corporates.objects.get(id=pk)
    #models.corporates.delete(modvar)
    modvar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])        
def updating(request,pk):
    try:
        modvar=models.corporates.objects.get(id=pk)
    except models.corporates.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET'     :
        servar=corpseri(modvar)
        return Response(servar.data)

    if request.method=='PUT':
        servar=corpseri(modvar,data=request.data)
        if servar.is_valid():
            servar.save()
            return Response(servar.data,status=status.HTTP_200_OK)
        return Response(servar.error,status=status.HTTP_400_BAD_REQUEST)    

    if request.method=='DELETE'    :
        modvar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class restlisting(APIView):
    def get(self,request):
        mv=models.corporates.objects.all()
        sv=corpseri(mv,many=True)
        return Response(sv.data)

    def post(self,request)    :
        sv=corpseri(data=request.data)
        if sv.is_valid():
            sv.save()
            return Response(sv.data,status=status.HTTP_201_CREATED)
        return Response(sv.error,status=status.HTTP_400_BAD_REQUEST)  


class restdetaillisting(APIView)          :
    def objectone(self,pk):
        try:
            return models.corporates.objects.get(id=pk)
        except models.corporates.DoesNotExist:
            raise Http404   

    def get(self,request,pk)         :
        mv=self.objectone(pk)
        sv=corpseri(mv)
        return Response(sv.data)

    def put(self,request,pk):
        mv=self.objectone(pk)
        sv=corpseri(mv,data=request.data)    
        if sv.is_valid():
            sv.save()
            return Response(sv.data,status=status.HTTP_200_OK)
        return Response(sv.error,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,pk)       :
        mv=self.objectone(pk)
        mv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
