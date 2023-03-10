from django.contrib import admin

from .models import Pet, Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']

@admin.register(Vaccine)
class Vaccine(admin.ModelAdmin):
    pass