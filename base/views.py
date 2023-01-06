from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'article.html')


def catergory(request):
    return render(request, 'category.html')


def about(request):
    return render(request,'about.html')

def docs(request):
    return  render(request , 'docs.html')