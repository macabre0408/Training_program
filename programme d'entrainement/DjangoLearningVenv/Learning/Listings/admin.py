from django.contrib import admin

from Listings.models import Band, Listings

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed')
    
admin.site.register(Band, BandAdmin)
admin.site.register(Listings, ListingAdmin)
