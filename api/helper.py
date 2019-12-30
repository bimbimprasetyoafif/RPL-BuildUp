from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, 
    ListCreateAPIView
)
from api.pagination import CustomPagination


respon = {}
respon['status']=0
respon['response']='NON AUTHORITATIVE'
# =================
# Overview
# =================

def get_all(self, request):
    data = self.get_queryset()

    paginate_queryset = self.paginate_queryset(data)
    serializer = self.serializer_class(paginate_queryset, many=True)
    if serializer == None:
            return Response(self.content, status=status.HTTP_404_NOT_FOUND)
    else:
        return self.get_paginated_response(serializer.data)

# cuman customre
def post_new(self, request):
    serializer = self.serializer_class(data=request.data)
    
    data = request.data
    data['creator'] = request.user.pk
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

# cuman toko dan vendor
def post_new_product_or_desain(self, request):
    serializer = self.serializer_class(data=request.data)
    if(request.user.role == 2 or request.user.role == 3):
        data = request.data
        data['creator'] = request.user.pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    else:
        return Response(respon, status=status.HTTP_401_UNAUTHORIZED)

def post_new_desain_rab_atau_material(self, request):
    serializer = self.serializer_class(data=request.data)
    if(request.user.role == 2):
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    else:
        return Response(respon, status=status.HTTP_401_UNAUTHORIZED)

# cuman admin
def post_Category(self, request):
    serializer = self.serializer_class(data=request.data)
    if(request.user.role == None):
        data = request.data
        data['creator'] = request.user.pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    else:        
        return Response(respon, status=status.HTTP_401_UNAUTHORIZED)


# =================
# Specific area
# =================

def get_specific(self, request, pk):
    try:
        data = self.get_queryset(pk) 
        
        serializer = self.serializer_class(data)
        
        if serializer == None:
            return Response(self.content, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
    except:        
        return Response(self.content, status=status.HTTP_404_NOT_FOUND)

def put_specific(self, request, pk):    
    data = self.get_queryset(pk)
    
    if(request.user == data.creator): # If creator is who makes request
        serializer = self.serializer_class(data, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)    
        

def delete_specific(self, request, pk, format=None):
    data = self.get_queryset(pk)

    if(request.user == data.creator): # If creator is who makes request
        data.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
    else:
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)