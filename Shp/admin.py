from Shp.models import categ, products
from django.contrib import admin

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(categ,catadmin)
class proadmin(admin.ModelAdmin):
    list_display = ['name','slug','stock','img','price','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,proadmin)