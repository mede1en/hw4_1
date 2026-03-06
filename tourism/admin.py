from django.contrib import admin
from .models import Person, Category, Tour, Booking, Review

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Booking)
admin.site.register(Review) 
