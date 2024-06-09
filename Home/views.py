from django.shortcuts import render , HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
def  index(request):
    # return HttpResponse("This  is HomePage  on View of Home")
    return render (request,"index.html")

def  about(request):
    # return HttpResponse("This  is About on View of Home")
     return render (request,"about.html")

def  contact(request):
    # return HttpResponse("This  is Contact Us on View of Home")
    if  request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')  
        password= request.POST.get('password')
        Phone=request.POST.get('Phone')  
        Suggetion= request.POST.get('Suggetion')
        obj =Contact(name=name,email=email,password=password,Phone=Phone,
                     date=datetime.today(),Suggetion=Suggetion)
        
        obj.save()

    return render (request,"contact.html")

def  services(request):
    # return HttpResponse("This  is About on View of Home")
     return render (request,"services.html")
