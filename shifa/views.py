from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def resume(request):
    return render(request,'resume.html')
def contact(request):
    return render(request,'contact.html')

