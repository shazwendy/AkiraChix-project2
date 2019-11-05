from django.db import models

from course.models import Course
import datetime
from django.core.exceptions import ValidationError
# courses = models.ManyToManyField(Course)


class Student(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  date_of_birth = models.DateField()
  gender = models.CharField(max_length = 20)
  registration_number = models.CharField(max_length = 20)
  email = models.EmailField(max_length = 70)
  phone_number = models.CharField(max_length = 15)
  date_joined = models.DateField()
  courses = models.ManyToManyField(Course,blank=True,related_name = "students")
  image = models.ImageField(upload_to = "profile_image", blank = True)

  def __str__(self):
  	return self.first_name + " " + self.last_name


  def full_name(self):
    return "{} {}".format(self.first_name, self.last_name)


  def get_age(self):
    today = datetime.date.today()
    return today.year - self.date_of_birth.year - ((today.month,today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
  age = property(get_age)

  def clean(self):
    age = self.age
    if age < 18 or age > 40 :
      raise ValidationError("You ought to be above 18 years and below 40 years in order to register")
    return age

  # def  full_name(self):
  #   return self.first_name


