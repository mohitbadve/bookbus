from django.db import models

class User(models.Model):

    username = models.CharField(max_length = 50,unique=True)
    email_id = models.CharField(max_length = 50,unique=True)
    password = models.CharField(max_length = 20)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    mob_no = models.CharField(max_length=10)
    type = models.CharField(max_length=1, default='C')

    @classmethod
    def create(cls, username,email_id,password,dob,address,pincode,mob_no,type):
        user = cls(username = username,email_id=email_id,password = password,dob =dob, address=address,pincode = pincode,mob_no=mob_no,type=type)
        return user

    class Meta:
        db_table = "user"


class Customer(models.Model):

    username = models.CharField(max_length = 50,unique=True)

    class Meta:
        db_table = "customer"


class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "admin"


class Bus(models.Model):

    bus_id = models.IntegerField(unique=True,blank=False)
    name = models.CharField(max_length=50,unique=True)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    no_of_seats = models.IntegerField()
    time = models.FloatField()
    description = models.CharField(max_length=10)

    @classmethod
    def create(cls, bus_id,name,source,destination,no_of_seats,time,description):
        bus = cls(bus_id = bus_id,name=name,source = source,destination =destination, no_of_seats=no_of_seats,time = time,description=description)
        return bus

    class Meta:
        db_table = "bus"

