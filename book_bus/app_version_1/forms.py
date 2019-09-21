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