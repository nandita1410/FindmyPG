from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from main.models import *

# Create your views here.
def index(request):
	loginid=request.session.get('loginid')
	if(loginid):
		data={}
		data['username']=Login.objects.get(pk=loginid).username
		data['profile']=Owner.objects.get(loginid=loginid)
		return render(request,'owner/index.html',data)
	else:
		return redirect('/owner/login')

def addpg(request):
	loginid=request.session.get('loginid')
	if(loginid and request.method=='GET'):
		data={}
		data['username']=Login.objects.get(id=loginid).username
		data['profile']=Owner.objects.get(loginid=loginid)
		return render(request,'owner/addpg.html',data)
	elif(request.method=='POST'):
		#PG

		obj=PG()	
		obj.address=request.POST.get('address')
		obj.location=request.POST.get('location')
		obj.city=request.POST.get('city')
		obj.pin=request.POST.get('pin')
		obj.rent=request.POST.get('rent')
		obj.occupancy=request.POST.get('occupancy')
		obj.forgender=request.POST.get('gender')
		obj.size=request.POST.get('size')
		obj.rooms=request.POST.get('rooms')
		obj.intime='2018-08-10 08:00'
		obj.outtime='2018-08-10 23:00'
		obj.ownerid=Owner.objects.get(loginid=loginid)

		obj.save()

		#Ameneties
		amn=Ameneties()
		amn.pgid=obj
		amn.ac=True if request.POST.get('ac')!=None else False
		amn.watercooler=True if request.POST.get('watercooler') else False
		amn.waterpurifier=True if request.POST.get('waterpurifier') else False
		amn.geyser=True if request.POST.get('geyser') else False
		amn.bed=True if request.POST.get('bed') else False
		amn.wifi=True if request.POST.get('wifi') else False
		amn.meals=True if request.POST.get('meals') else False
		amn.parking=True if request.POST.get('parking') else False
		amn.save()

		#PG Images
		files=request.FILES.getlist('pgimages')
		for f in files:
			pgimages=PGImages()
			pgimages.pgid=obj
			pgimages.image=f
			pgimages.save()

		loginid=request.session.get('loginid')
		data={}
		data['username']=Login.objects.get(pk=loginid).username
		data['profile']=Owner.objects.get(loginid=loginid)
		data['success']=True
		return render(request,'owner/addpg.html',data)
	else:
		return redirect('/owner/login')

def register(request):
	if(request.method=='GET'):
		return render(request,'owner/register.html',None)
	else:
		username=request.POST.get('username')
		password=request.POST.get('password')

		#Check if Credentials already exists
		if(Login.objects.filter(username=username).exists()):
			data={}
			data['error']='User already exists'
			return render(request,'owner/register.html',data)

		obj=Login()	
		obj.username=username
		obj.password=password
		obj.logintype='Owner'
		obj.save()

		profile=Owner()
		profile.loginid=obj
		profile.name='User'
		profile.address='NA'
		profile.phone=0
		profile.email='NA'
		profile.photo='male.jpg'
		profile.save()

		data={}
		data['success']=True
		return render(request,'owner/register.html',data)


def login(request):
	if(request.method=='GET'):
		return render(request,'owner/login.html',None)
	else:
		username=request.POST.get('username')
		password=request.POST.get('password')

		#Check if Credentials already exists
		if(not Login.objects.filter(username=username,password=password).exists()):
			data={}
			data['error']='Username and/or Password Not exists'
			return render(request,'owner/login.html',data)

		obj=Login.objects.get(username=username,password=password)	
		request.session['loginid']=obj.id
		return redirect('/owner')

def profile(request):
	loginid=request.session.get('loginid')
	if(loginid and request.method=='GET'):
		data={}
		data['username']=Login.objects.get(id=loginid).username
		data['profile']=Owner.objects.get(loginid=loginid)
		return render(request,'owner/profile.html',data)
	elif(loginid and request.method=='POST'):
		data={}
		data['username']=Login.objects.get(pk=loginid).username
		owner=Owner.objects.get(loginid=loginid)
		owner.name=request.POST.get('name')
		owner.address=request.POST.get('address')
		owner.phone=request.POST.get('phone')
		owner.email=request.POST.get('email')
		owner.save()
		data['profile']=owner
		data['success']=True
		return render(request,'owner/profile.html',data)		
	else:
		return redirect('/owner/login/')

def ProfilePhoto(request):
	loginid=request.session.get('loginid')
	owner=Owner.objects.get(loginid=loginid)
	owner.photo=request.FILES.get('photo')
	owner.save()
	return redirect('/owner/')		

def logout(request):
	del request.session['loginid']
	return redirect('/owner/')


def pglist(request):
	loginid=request.session.get('loginid')
	if(loginid and request.method=='GET'):
		data={}
		data['username']=Login.objects.get(id=loginid).username
		data['profile']=Owner.objects.get(loginid=loginid)
		owner=Owner.objects.get(loginid=loginid)
		pgs=PG.objects.filter(ownerid=owner)
		data['pgs']=pgs
		return render(request,'owner/pglist.html',data)


def deletepg(request,id):
	pg=PG.objects.get(id=id)
	pg.delete()
	return redirect('/owner/pgs/')


def updatepg(request,id):
	pg=PG.objects.get(id=id)
	amn=Ameneties.objects.get(pgid=pg.id)

	if(request.method=='GET'):
		loginid=request.session.get('loginid')
		if(loginid):
			data={}
			data['username']=Login.objects.get(pk=loginid).username
			data['profile']=Owner.objects.get(loginid=loginid)
			data['pg']=pg
			data['ameneties']=amn
		return render(request,'owner/updatepg.html',data)
	else:
		pg.address=request.POST.get('address')
		pg.location=request.POST.get('location')
		pg.city=request.POST.get('city')
		pg.pin=request.POST.get('pin')
		pg.rent=request.POST.get('rent')
		pg.occupancy=request.POST.get('occupancy')
		pg.forgender=request.POST.get('gender')
		pg.size=request.POST.get('size')
		pg.rooms=request.POST.get('rooms')

		pg.save()

		#Ameneties
		amn.ac=True if request.POST.get('ac')!=None else False
		amn.watercooler=True if request.POST.get('watercooler') else False
		amn.waterpurifier=True if request.POST.get('waterpurifier') else False
		amn.geyser=True if request.POST.get('geyser') else False
		amn.bed=True if request.POST.get('bed') else False
		amn.wifi=True if request.POST.get('wifi') else False
		amn.meals=True if request.POST.get('meals') else False
		amn.parking=True if request.POST.get('parking') else False

		amn.save()

		data={}
		loginid=request.session.get('loginid')
		data['username']=Login.objects.get(pk=loginid).username
		data['profile']=Owner.objects.get(loginid=loginid)
		data['pg']=pg
		data['ameneties']=amn
		data['success']=True
		return render(request,'owner/updatepg.html',data)


def Notifications(request):
	loginid=request.session.get('loginid')
	owner=Owner.objects.get(loginid=loginid)
	pgs=PG.objects.filter(ownerid=owner)

	data={}
	data['username']=Login.objects.get(id=loginid).username
	data['profile']=Owner.objects.get(loginid=loginid)
	data['enquiries']=[]
	
	if(loginid and request.method=='GET'):
		enquiries=ContactOwner.objects.filter()
		
		for enquiry in enquiries:		
			for pg in pgs:
				if(enquiry.pgid==pg):
					data['enquiries'].append(enquiry)

		return render(request,'owner/notifications.html',data)