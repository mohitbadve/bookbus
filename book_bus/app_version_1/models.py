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
    time = models.TimeField()
    description = models.CharField(max_length=10)
    availability = models.CharField(default='A',max_length=1)
    available_seats = models.IntegerField(default=no_of_seats)

    @classmethod
    def create(cls, bus_id,name,source,destination,no_of_seats,time,description,availability,available_seats):
        bus = cls(bus_id = bus_id,name=name,source = source,destination =destination, no_of_seats=no_of_seats,time = time,description=description,availability=availability,available_seats=available_seats)
        return bus

    class Meta:
        db_table = "bus"


class Seat(models.Model):
    # bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    bus_id = models.IntegerField()
    seat_row = models.IntegerField()
    seat_col = models.IntegerField()

    @classmethod
    def create(cls, bus_id, seat_row, seat_col):
        seat = cls(bus_id=bus_id, seat_row=seat_row, seat_col=seat_col)
        return seat

    class Meta:
        db_table = "seat"

class Transaction(models.Model):
    trans_id = models.IntegerField()
    amt = models.FloatField()
    bus_id = models.IntegerField()
    seat_row = models.IntegerField()
    seat_col = models.IntegerField()

    @classmethod
    def create(cls, trans_id,amt, bus_id, seat_row, seat_col):
        trans = cls(trans_id=trans_id,amt=amt, bus_id=bus_id, seat_row=seat_row, seat_col=seat_col)
        return trans

    class Meta:
        db_table = "trans"




