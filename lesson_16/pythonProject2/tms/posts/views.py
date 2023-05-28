from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL= "D:\Python\pythonProject1"
response_ = requests.get(os.environ.get("URL"))
POSTS = response_.json()


def home(request):
    return render(request, 'home.html', {'posts': POSTS})


def posts(request):
    return JsonResponse({'posts': POSTS})
