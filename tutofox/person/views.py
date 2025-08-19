from django.shortcuts import render
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PersonModel
from .serializers import PersonSerializer

# Create your views here.
class PersonApiView(APIView):
    def get(self, request):
        serializer = PersonSerializer(PersonModel.objects.all(), many= True)
        return Response(status=status.HTTP_200_OK, data = serializer.data)
    def post(self, request):
        #res = request.data.get('name')
        serializer= PersonSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data= serializer.data)
    
class PersonApiViewDetail(APIView):
    def get_object(self,pk):
        try:
            return PersonModel.objects.get(pk=pk)
        except PersonModel.DoesNotExist:
            return None
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PersonSerializer(post)
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    def put(self, request, pk):
        post = self.get_object(pk)
        if(post is None):
            return Response(status= status.HTTP_200_OK, data= {'error':'Not found data'})
        serializer = PersonSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_200_OK, data = serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        response = {'deleted': True}
        return Response(status= status.HTTP_200_OK, data= response)