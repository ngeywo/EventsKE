from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event


# Register your models here.
#admin.site.register(Venue)
admin.site.register(MyClubUser)

#admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display=('name','region','address','phone_number',)
	ordering =('name',)
	search_fields=('name','address','region',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields=(('name','venue'),'event_date','description','manager',)
	list_display=('name','event_date','venue',)
	list_filter= ('event_date','venue',)
	search_fields=('name','venue',)
	ordering=('-event_date',)


