from django.shortcuts import render

# Create your views here.


# Home page
def index(request):
    return render(request,'index.html')
