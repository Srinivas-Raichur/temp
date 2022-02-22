
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class view_post(APIView):
    def post(self,request):
        data = request.data
        print(data)

        return Response({"status":201,"msg":"ok"},status=status.HTTP_201_CREATED)