from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core.mail import mail_admins
from folio.models import  MyInfo 
from blog.models import *
from .forms import Contact_me_form
# Create your views here.

def base():
    """helper function to obtain several querysets from the models"""
    prof = Profile.objects.get()
    langs = Lang.objects.all()
    inter = Interests.objects.all()
    return {
        'profile': prof,
        'langg': langs,
        'intrsts': inter,
        'profile': prof,
    }
def index(request):
    edu = Education.objects.all()
    exp = Experience.objects.all()
    context={
        'education': edu,
        'experience': exp,
    }
    context["b"]=base()
    return render(request,"resume/index.html",context)
def resm(request):
    edu = Education.objects.all()
    exp = Experience.objects.all()
    skl=Skill.objects.all()
    context={
        'education': edu,
        'experience': exp,
        'skill': skl,
    }
    context["b"]=base()
    return render(request,"resume/resum.html",context)
def portfolio(request):
    projects=MyInfo.objects.all()

    context={'obj':projects,}
    context["b"]=base()
    return render(request,"resume/portfolio.html",context)    
    
def blog(request):
    pst = Post.objects.filter().order_by('-created_on')
    comm=Comment.objects.all()
    
    context={'posts':pst,'comments':comm,}
    context["b"]=base()
    return render(request,"resume/blog.html",context)

def contact(request):
   if request.method == "POST":

       form = Contact_me_form(request.POST)

       if form.is_valid():
           #create commnt object but dont save to the database yet
            form.save(commit=True)
            data=request.POST.copy()
            name=data.get("email")
            message=data.get("message")
           
                
            mail_admins(subject='name',message='message')
            form = Contact_me_form()
            
   else:
     form=Contact_me_form()
   context={'form':form,}
   context["b"]=base()  
   return render(request,"resume/contact.html",context)
     
   

