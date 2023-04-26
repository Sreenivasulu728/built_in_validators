from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            return HttpResponse('data inserted successfully')
        else:
            return HttpResponse('invalid data')
    

    return render(request,'topic_name.html',d)