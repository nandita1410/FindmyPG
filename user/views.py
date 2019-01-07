from django.shortcuts import render,redirect
from main.models import *
from django.http import HttpResponse

def index(request):
	pgs=PG.objects.filter()
	pgs=pgs[:5]

	for i in range(len(pgs)):
		pgimages=PGImages.objects.filter(pgid=pgs[i])
		if(len(pgimages)!=0):
			pgs[i].image=pgimages[0].image
		amn=Ameneties.objects.get(pgid=pgs[i])
		pgs[i].ameneties=[]
		if(amn.ac==True):
			pgs[i].ameneties.append('AC')
		if(amn.watercooler==True):
			pgs[i].ameneties.append('Water Cooler')
		if(amn.waterpurifier==True):
			pgs[i].ameneties.append('Water Purifier')
		if(amn.geyser==True):
			pgs[i].ameneties.append('Geyser')
		if(amn.bed==True):
			pgs[i].ameneties.append('Bed')
		if(amn.wifi==True):
			pgs[i].ameneties.append('WiFi')
		if(amn.meals==True):
			pgs[i].ameneties.append('Meals')
		if(amn.parking==True):
			pgs[i].ameneties.append('Parking')


	data={'pgs':pgs}
	return render(request,'user/index.html',data)

def search(request,page=1):

	if(request.method=='GET'):
		pgs=PG.objects.filter()

		totalrecords=len(PG.objects.filter())
		searchrecords=len(pgs)

		pagesize=6
		nopages=int(searchrecords/pagesize)+1 if int(searchrecords%pagesize)!=0 else int(searchrecords/pagesize)

		if(page==None):
			page=1

		pgs=pgs[(page-1)*6:page*6]
		for i in range(len(pgs)):
			pgimages=PGImages.objects.filter(pgid=pgs[i])
			if(len(pgimages)!=0):
				pgs[i].image=pgimages[0].image
			amn=Ameneties.objects.get(pgid=pgs[i])
			pgs[i].ameneties=[]
			if(amn.ac==True):
				pgs[i].ameneties.append('AC')
			if(amn.watercooler==True):
				pgs[i].ameneties.append('Water Cooler')
			if(amn.waterpurifier==True):
				pgs[i].ameneties.append('Water Purifier')
			if(amn.geyser==True):
				pgs[i].ameneties.append('Geyser')
			if(amn.bed==True):
				pgs[i].ameneties.append('Bed')
			if(amn.wifi==True):
				pgs[i].ameneties.append('WiFi')
			if(amn.meals==True):
				pgs[i].ameneties.append('Meals')
			if(amn.parking==True):
				pgs[i].ameneties.append('Parking')


		data={'pgs':pgs,'totalrecords':totalrecords,'searchrecords':searchrecords,'nopages':range(1,nopages+1)}
		return render(request,'user/search.html',data)
	else:
		location=request.POST.get('location')
		gender=request.POST.get('forgender')
		price=request.POST.get('price')
		occupancy=request.POST.get('occupancy')

		if(location!=""):			
			pgLocation=set(PG.objects.filter(location=location))
		else:
			pgLocation=set(PG.objects.filter())

		if(gender!='Gender'):
			pgGender=set(PG.objects.filter(forgender=gender))
		else:
			pgGender=set(PG.objects.filter())

		if(price!='Price'):
			min=0
			max=99999
			if(price=="1"):
				min=1000
				max=3000
			elif(price=="2"):
				min=3000
				max=6000
			elif(price=="3"):
				min=6000
				max=10000
			elif(price=="4"):
				min=10000
				max=99999
			pgPrice=set(PG.objects.filter(rent__gte=min,rent__lte=max))
		else:
			pgPrice=set(PG.objects.filter())


		if(occupancy!='Occupancy'):
			min=0
			max=99
			if(occupancy=="1"):
				min=0
				max=5
			elif(occupancy=="2"):
				min=5
				max=10
			elif(occupancy=="3"):
				min=10
				max=99

			pgOccupancy=set(PG.objects.filter(occupancy__gte=min,occupancy__lte=max))
		else:
			pgOccupancy=set(PG.objects.filter())

		pgs=set(PG.objects.filter())
		pgs=pgs.intersection(pgLocation)
		pgs=pgs.intersection(pgGender)
		pgs=pgs.intersection(pgPrice)
		pgs=pgs.intersection(pgOccupancy)
		pgs=list(pgs)

		totalrecords=len(PG.objects.filter())
		searchrecords=len(pgs)

		pagesize=6
		nopages=int(searchrecords/pagesize)+1 if int(searchrecords%pagesize)!=0 else int(searchrecords/pagesize)

		if(page==None):
			page=1

		pgs=pgs[(page-1)*6:page*6]

		for i in range(len(pgs)):
			pgimages=PGImages.objects.filter(pgid=pgs[i])
			if(len(pgimages)!=0):
				pgs[i].image=pgimages[0].image
			amn=Ameneties.objects.get(pgid=pgs[i])
			pgs[i].ameneties=[]
			if(amn.ac==True):
				pgs[i].ameneties.append('AC')
			if(amn.watercooler==True):
				pgs[i].ameneties.append('Water Cooler')
			if(amn.waterpurifier==True):
				pgs[i].ameneties.append('Water Purifier')
			if(amn.geyser==True):
				pgs[i].ameneties.append('Geyser')
			if(amn.bed==True):
				pgs[i].ameneties.append('Bed')
			if(amn.wifi==True):
				pgs[i].ameneties.append('WiFi')
			if(amn.meals==True):
				pgs[i].ameneties.append('Meals')
			if(amn.parking==True):
				pgs[i].ameneties.append('Parking')


		data={'pgs':pgs,'totalrecords':totalrecords,'searchrecords':searchrecords,'nopages':range(1,nopages+1)}
		return render(request,'user/search.html',data)


def PGDetail(request,pgid=1):
	pg=PG.objects.get(id=pgid)	
	owner=pg.ownerid

	pg.image=PGImages.objects.filter(pgid=pg)[:1][0]
	pg.images=PGImages.objects.filter(pgid=pg)[1:4]
	amn=Ameneties.objects.get(pgid=pg)
	pg.ameneties=[]
	if(amn.ac==True):
		pg.ameneties.append('AC')
	if(amn.watercooler==True):
		pg.ameneties.append('Water Cooler')
	if(amn.waterpurifier==True):
		pg.ameneties.append('Water Purifier')
	if(amn.geyser==True):
		pg.ameneties.append('Geyser')
	if(amn.bed==True):
		pg.ameneties.append('Bed')
	if(amn.wifi==True):
		pg.ameneties.append('WiFi')
	if(amn.meals==True):
		pg.ameneties.append('Meals')
	if(amn.parking==True):
		pg.ameneties.append('Parking')


	data={'pg':pg,'owner':owner}
	return render(request,'user/pgdetail.html',data)


def Contact(request,pgid):
	contact=ContactOwner()
	contact.pgid=PG.objects.get(id=pgid)
	contact.name=request.POST.get('name')
	contact.email=request.POST.get('email')
	contact.phone=request.POST.get('phone')
	contact.message=request.POST.get('message')
	contact.datetime='2018-01-01'
	contact.save()
	return redirect("/")