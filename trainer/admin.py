from django.contrib import admin

from .models import Trainer

class TrainerAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","email","course_teaching")
	search_fields = ("first_name","last_name","course_teaching")

	
admin.site.register(Trainer,TrainerAdmin)
# Register your models here.
