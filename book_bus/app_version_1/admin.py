from django.contrib import admin
from app_version_1.models import User, Bus, Seat, Transaction

admin.site.register(Transaction)
admin.site.register(User)
admin.site.register(Bus)
admin.site.register(Seat)

