from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    logintype=models.CharField(max_length=30)

class Owner(models.Model):
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField(max_length=30)
    photo=models.FileField()

class User(models.Model):
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField(max_length=30)
    photo=models.FileField()

class PG(models.Model):
    ownerid=models.ForeignKey(Owner, on_delete=models.CASCADE)
    address=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pin=models.IntegerField()
    rent=models.DecimalField(max_digits=10,decimal_places=2)
    occupancy=models.IntegerField()
    forgender=models.CharField(max_length=30)
    size=models.IntegerField()
    rooms=models.IntegerField()
    intime=models.DateTimeField()
    outtime=models.DateTimeField()

class Ameneties(models.Model):
    pgid=models.ForeignKey(PG,on_delete=models.CASCADE)
    ac=models.BooleanField()
    watercooler=models.BooleanField()
    waterpurifier=models.BooleanField()
    geyser=models.BooleanField()
    bed=models.BooleanField()
    wifi=models.BooleanField()
    meals=models.BooleanField()
    parking=models.BooleanField()

class Favourites(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    pgid=models.ForeignKey(PG,on_delete=models.CASCADE)

class Ratings(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    pgid=models.ForeignKey(PG,on_delete=models.CASCADE)
    rating=models.IntegerField()
    review=models.CharField(max_length=30)
    date=models.DateField()

class ContactOwner(models.Model):
    pgid=models.ForeignKey(PG,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    message=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    datetime=models.DateTimeField()

class PGImages(models.Model):
	pgid=models.ForeignKey(PG,on_delete=models.CASCADE)
	image=models.FileField()
