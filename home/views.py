from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':'this is sent1',
        'variable2':'this is sent2'
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")