from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, 
    ListCreateAPIView
)

# =================
# Overview
# =================


def get_all(self, request):
    data = self.get_queryset()
    serializer = self.serializer_class(data, many=True)
    return Response(serializer.data)

def post_new(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


# =================
# Specific area
# =================

def get_specific(self, request, pk):
    data = self.get_queryset(pk) 
    serializer = self.serializer_class(data)
    if serializer == None:
        return Response(self.content, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.data, status=status.HTTP_200_OK)

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