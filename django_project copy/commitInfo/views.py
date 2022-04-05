from django.shortcuts import render
from datetime import datetime
import re
from commitInfo.models import commitInfo
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def test_url(request):
    return HttpResponse("Hello, test-page!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def commit_templates(request):
    return render(
        request,
        'commitInfo/commitInfo.html'
    )

def check_db(request):
    res = commitInfo.objects.all()
    context = {'res': res}
    return render (
        request,'commitInfo/commitInfo.html',context
    )