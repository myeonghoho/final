from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "main.html")

def man(request):
    return render(request, "man/man.html")

def woman(request):
    return render(request, "woman/woman.html") 

def upload(request):
    return render(request, "upload.html")