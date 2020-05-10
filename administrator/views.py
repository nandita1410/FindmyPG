from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import *

# Create your views here.
def index(request):
	loginid=request.session.get('isloggedin')	
	if(loginid and request.method=='GET'):
		data={}
		pgs=PG.objects.filter()
		data['pgs']=pgs
		return render(request,'administrator/pglist.html',data)
	else:
		return redirect('/admin/login/')


def login(request):
	if(request.method=='GET'):
		return render(request,'administrator/login.html',None)
	else:
		username=request.POST.get('username')
		password=request.POST.get('password')
		if(username!='admin' and password!='password'):
			data={}
			data['error']='Username and/or Password Not exists'
			return render(request,'administrator/login.html',data)
		request.session['isloggedin']=True
		return redirect('/admin/')


def logout(request):
	del request.session['isloggedin']
	return redirect('/admin/')


def pglist(request):
	loginid=request.session.get('isloggedin')
	if(loginid and request.method=='GET'):
		data={}
		pgs=PG.objects.all()
		data['pgs']=pgs
		return render(request,'administrator/pglist.html',data)



def verify(request,id):
	pg=PG.objects.get(id=id)
	pg.isverified=True
	pg.save()
	return redirect('/admin/pglist/') 

