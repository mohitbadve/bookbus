from django.shortcuts import render, redirect, get_object_or_404
from app_version_1.forms import LoginForm, UserForm, BusForm, ForgotPasswordForm, SearchBusForm, SeatForm, TransactionForm, ChangePasswordForm
from app_version_1.models import User, Bus, Seat, Transaction
import sys
from django.conf import settings
from django.core.mail import send_mail

session_username = ''

def home(request):
    if(session_username != ''):
        bus = Bus.objects.all()
        return render(request, 'login_ui.html', {'username': session_username,'bus':bus})
    return render(request,'login_ui.html',{'username':session_username})

def login(request):
    try:
        login_data = LoginForm(request.POST)
        username = login_data.data['username']
        password = login_data.data['password']
        user = get_object_or_404(User, username = username, password = password)
        print(user)
        global session_username
        session_username = username
        return redirect(to='http://127.0.0.1:8000/form-bus')
    except:
        return render(request, 'e403.html')

def registerForm(request):
    return render(request,'register_ui.html')

def register(request):
    try:
        user_data = UserForm(request.POST)
        email_id = user_data.data['email_id']
        password = user_data.data['password']
        dob = user_data.data['dob']
        address = user_data.data['address']
        pincode = user_data.data['pincode']
        mob_no = user_data.data['mob_no']
        type = 'C'
        username = email_id
        print(email_id)
        print(password)
        print(username)
        user = User.create(email_id=email_id,password=password,username=username,dob=dob,address=address,pincode=pincode,mob_no=mob_no,type=type)
        user.save()
        # user = get_object_or_404(User, username = username, password = password)
        print(user)
        send_mail(
            'Registration for BookBus',
            'Dear '+username + '\n\nWelcome to BookBus\n\nHere you can search and book buses based on various filters',
            settings.EMAIL_HOST_USER,
            ['mohit.badve@spit.ac.in', username],
            fail_silently=False,
        )
        return render(request,'login_ui.html',{'username':'registered'})
    except:
        return render(request, 'e404.html')

def addBusForm(request):
    bus_id = Bus.objects.all().count() + 1
    return render(request, 'add_bus_form_ui.html', {'bus_id': bus_id,'username':session_username})

def busForm(request):
    bus = Bus.objects.all()
    return render(request,'bus_form_ui.html',{'bus':bus,'username':session_username})
    #return render(request,'bus_form.html',{'bus': bus,'username':session_username})

def addBus(request):
    try:
        bus_data = BusForm(request.POST)
        print(bus_data.data['bus_id'])
        bus_id = bus_data.data['bus_id']
        name = bus_data.data['name']
        source = bus_data.data['source']
        destination = bus_data.data['destination']
        no_of_seats = int(bus_data.data['no_of_seats'])
        time = bus_data.data['time']
        description = bus_data.data['description']
        availability = 'A'
        available_seats = no_of_seats

        #NEWNWEWDS
        no_of_rows = int(bus_data.data['no_of_rows'])
        no_of_columns = int(bus_data.data['no_of_columns'])
        seat = bus_data.data['seat_data']
        seat_cal = seat.split(" ")[:-1]
        bus = Bus.create(bus_id = bus_id,name=name,source = source,destination =destination, no_of_seats=no_of_seats,time = time,
                         description=description,availability=availability,available_seats=available_seats, no_of_columns=no_of_columns, no_of_rows=no_of_rows)
        for i in seat_cal:
            temp = i.split("-")
            row = int(temp[0])
            col = int(temp[1])
            seat = Seat.create(bus_id=bus_id,seat_row=row,seat_col=col,seat_status="A")
            seat.save()
        bus.save()
        print(bus)
        return redirect(to='http://127.0.0.1:8000/form-bus')
    except Exception as e:
        print(e)
        return render(request, 'e404.html')


def formUpdateBus(request,b_id):
    if(session_username != ''):
        try:
            bus_id = b_id
            print(bus_id)
            bus = get_object_or_404(Bus,bus_id = bus_id)
            print(bus.time)
            return render(request,'update_bus_ui.html',{'bus':bus,'username':session_username})
        except:
            return render(request,'update_bus_ui.html',{'username' : session_username})
    else:
        return render(request, 'update_bus_ui.html', {'username': session_username})

def updateBus(request):
    try:
        bus_data = BusForm(request.POST)
        print(bus_data.data['bus_id'])
        bus_id = bus_data.data['bus_id']
        name = bus_data.data['name']
        source = bus_data.data['source']
        destination = bus_data.data['destination']
        no_of_seats = int(bus_data.data['no_of_seats'])
        time = bus_data.data['time']
        description = bus_data.data['description']
        availability = 'A'
        bus = get_object_or_404(Bus,bus_id=bus_id)
        bus.name = name
        bus.source = source
        bus.destination = destination
        bus.no_of_seats = no_of_seats
        bus.available_seats = no_of_seats
        bus.time = time
        bus.description = description
        bus.availability = availability
        bus.save()
        return redirect(to='http://127.0.0.1:8000/form-bus')
    except:
        return render(request,'e404.html')


def deleteBus(request,b_id):
    if(session_username != ''):
        try:
            bus_id = b_id
            bus = get_object_or_404(Bus,bus_id=bus_id)
            bus.availability = 'N'
            bus.save()
            return redirect(to='http://127.0.0.1:8000/form-bus')
        except:
            return render(request,'e404.html')
    else:
        return redirect(to='http://127.0.0.1:8000/')

def formForgotPassword(request):
    return render(request,'forgot_password.html',{'submit':'False'})

def forgotPassword(request):
    try:
        user = ForgotPasswordForm(request.POST)
        print(user.data['username'])
        email_id = user.data['username']
        u = User.objects.all().filter(username=email_id).first()
        if u.username == email_id:
            send_mail(
                'Password Retrieval',
                'Dear ' + email_id + '\n\nWelcome to BookBus\n\n' + 'Your password : ' + u.password,
                settings.EMAIL_HOST_USER,
                ['mohit.badve@spit.ac.in', email_id],
                fail_silently=False,
            )
            return render(request,'forgot_password.html',{'submit':'True'})
        return render(request, 'e404.html')
    except:
        return render(request, 'e403.html')




def formSearchBus(request):
    return render(request,'search_bus_ui.html',{'query':'False'})

def searchBus(request):
    bus_list = SearchBusForm(request.POST)
    name = bus_list.data['name']
    source = bus_list.data['source']
    destination = bus_list.data['destination']
    time = bus_list.data['time']
    buses = Bus.objects.all().filter(availability='A')
    if name != '':
        buses = buses.filter(name=name)
        print(buses)
    if source != '':
        buses = buses.filter(source=source)
        print(buses)

    if destination !='':
        buses = buses.filter(destination=destination)
        print(buses)

    if time != '':
        buses = buses.filter(time=time)
        print(buses)

    print(buses)
    return render(request,'search_bus_ui.html',{'query':'True','bus':buses})









def seat(request,b_id):
    bus_id = b_id
    seats = Seat.objects.filter(bus_id=bus_id)
    bus = Bus.objects.get(bus_id=bus_id,availability='A')
    col = bus.no_of_columns
    row = bus.no_of_rows
    return render(request, 'seat.html', {"seats": seats, "bus": bus, "col": range(1, col + 1), "row": range(1, row + 1)})

def transaction(request,b_id):
    calculated_amount = 0
    if request.method == "POST":
        trans_data = TransactionForm(request.POST)
        amt = trans_data.data['amount']
        seat = trans_data.data['seat_data']
        seat_cal = seat.split(" ")[:-1]
        calculated_amount = 0
        seat_price = 10
        for i in seat_cal:
            calculated_amount = calculated_amount + seat_price
        bus_id = b_id
        bus = Bus.objects.get(bus_id=bus_id,availability='A')
        bus.available_seats = bus.available_seats - len(seat_cal)
        amt = trans_data.data['amount']
        trans_id = Transaction.objects.all().count()+1

        if float(amt) == float(calculated_amount):

            for i in seat_cal:
                temp = i.split("-")
                row = int(temp[0])
                col = int(temp[1])
                seat = Seat.objects.get(bus_id=bus.bus_id, seat_row=row,seat_col=col)
                seat.seat_status = "N"
                trans = Transaction.create(trans_id=trans_id,bus_id=bus.bus_id, seat_row=row, seat_col=col, amt=amt)
                trans.save()
                seat.save()

            bus.save()

            return render(request, 'success.html', {"username": row, 'password': col})
        else:
            return render(request, 'e404.html')
    else:
        seat_form = SeatForm(request.GET)
        seat = seat_form.data['seat_data']
        seat_cal = seat.split(" ")[:-1]
        bus_id = b_id
        seat_price = 10
        calculated_amount = 0
        for i in seat_cal:
            calculated_amount = calculated_amount + seat_price

        return render(request, 'transaction.html', {'seats':seat, "amt": calculated_amount,'bus_id':bus_id})






def logout(request):
    global session_username
    session_username = ''
    return redirect(to='http://127.0.0.1:8000/')

def formChangePassword(request):
    return render(request,'change_password.html',{'submit' : 'False'})

def changePassword(request):
    try:
        user = ChangePasswordForm(request.POST)
        print(user.data['username'])
        email_id = user.data['username']
        old_password = user.data['old_password']
        new_password = user.data['new_password']
        u = User.objects.all().filter(username=email_id,password=old_password).first()
        if u.username == email_id and u.password == old_password:
            changedUser = get_object_or_404(User,email_id = u.username)
            changedUser.password = new_password
            send_mail(
                'Changed Password',
                'Dear ' + email_id + '\n\nWelcome to BookBus\n\n' + 'Your new password : ' + new_password,
                settings.EMAIL_HOST_USER,
                ['mohit.badve@spit.ac.in', email_id],
                fail_silently=False,
            )
            changedUser.save()
            return render(request, 'change_password.html', {'submit': 'True'})
        return render(request, 'e404.html')
    except:
        return render(request, 'e403.html')