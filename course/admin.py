from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","description","start_date")
	search_fields = ("name","start_date")

	
admin.site.register(Course,CourseAdmin)

# Register your models here.
