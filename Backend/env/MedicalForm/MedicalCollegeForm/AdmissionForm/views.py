from django.shortcuts import render
from .serializers import ApplicationStudentSerializer, AdmissionStudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from .models import StudentModel

# from rest_framework.generics import (
#     CreateAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
# )


class ApplicationFormCreate(APIView):
    def post(self, request):
        serializer = ApplicationStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdmissionFormCreate(APIView):
    def post(self, request):
        serializer = AdmissionStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationFormUpdate(APIView):
    def put(self, request, pk):
        instance = StudentModel.objects.get(email=pk)
        serializer = ApplicationStudentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdmissionFormUpdate(APIView):
    def put(self, request, pk):
        instance = StudentModel.objects.get(email=pk)
        serializer = AdmissionStudentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationFormRetrieve(APIView):
    def get(self, request, pk):
        instance = StudentModel.objects.get(email=pk)
        serializer = ApplicationStudentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdmissionFormRetrieve(APIView):
    def get(self, request, pk):
        instance = StudentModel.objects.get(email=pk)
        serializer = AdmissionStudentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
