from django import forms

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 20)
   password = forms.CharField(widget = forms.PasswordInput())

class UserForm(forms.Form):
   email_id = forms.CharField(max_length = 20)
   dob = forms.DateField()
   address = forms.CharField(max_length=100)
   pincode = forms.CharField(max_length=6)
   mob_no = forms.CharField(max_length=10)
   password = forms.CharField(widget = forms.PasswordInput())

class BusForm(forms.Form):
   bus_id = forms.IntegerField()
   name = forms.CharField(max_length=50)
   source = forms.CharField(max_length=20)
   destination = forms.CharField(max_length=20)
   no_of_seats = forms.IntegerField()
   time = forms.TimeField()
   description = forms.CharField(max_length=10)
   availability = forms.CharField(max_length=1)

   #ASDJASDJASD
   no_of_rows = forms.IntegerField()
   no_of_columns = forms.IntegerField()
   seat_data = forms.CharField()

class ForgotPasswordForm(forms.Form):
   email_id = forms.CharField(max_length=20)

class SearchBusForm(forms.Form):
   name = forms.CharField(max_length=50)
   source = forms.CharField(max_length=20)
   destination = forms.CharField(max_length=20)
   no_of_seats = forms.IntegerField()
   time = forms.TimeField()

class SeatForm(forms.Form):
   seat_data = forms.CharField()

class TransactionForm(forms.Form):
   seat_data = forms.CharField()
   amt = forms.FloatField()


class ChangePasswordForm(forms.Form):
   email_id = forms.CharField(max_length=20)
   old_password = forms.CharField(widget = forms.PasswordInput())
   new_password = forms.CharField(widget = forms.PasswordInput())
