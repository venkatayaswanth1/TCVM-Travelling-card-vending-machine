from django.contrib import admin
from django.contrib.auth.models import User
#from django.contrib.auth.models import customer
from .models import customer
from .models import Transaction

# Register your models here.
#admin.site.register(user)
admin.site.register(customer)
admin.site.register(Transaction)