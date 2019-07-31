from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'../templates/polls/homepage.html')
    # return HttpResponse("Hello django,you are at prolls index.")