from django.shortcuts import render
from .models import Newappdetails
from .forms import Newappform
from django.db.models import Q

# Create your views here.
def display(request):
	newappdetails=Newappdetails.objects.all()
	return render(request,'display.html',{'newappdetails': newappdetails})

def insertnewapp(request):
	if request.method == "POST":
		form=Newappform(request.POST)
		form.save()
		return render(request,'display2.html',{'form': form})
	else:
		form=Newappform()
		return render(request,'display2.html',{'form': form})

def enter(request,decription):
	newappdetails=Newappdetails.objects.filter(Q(title__contains=decription) | Q(content__contains=decription))
	return render(request,'display.html',{'newappdetails':newappdetails})