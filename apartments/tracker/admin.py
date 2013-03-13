from django.contrib import admin
from models import Apartment, Pro, Con


#class ProConInline(admin.TabularInline):
    #model = ProCon

#class ApartmentAdmin(admin.ModelAdmin):
    #inlines = [
        #ProConInline,
    #]


#admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Apartment)

#class ProConAdmin(admin.ModelAdmin):
    ## list_filter = ('apartment',)
    #list_display = ('name', 'is_pro', )
#admin.site.register(ProCon, ProConAdmin)

admin.site.register(Pro)
admin.site.register(Con)
