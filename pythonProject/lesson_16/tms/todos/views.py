from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = "D:\Python\lesson\pythonProject"
response_ = requests.get(os.environ.get("URL"))
TODOS = response_.json()


def home(request):
    return render(request, 'home.html', {'todos': TODOS})


def posts(request):
    return JsonResponse({'todos': TODOS})
