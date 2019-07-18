from django.db import models


class Trainer(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  date_joined = models.DateField()
  gender = models.CharField(max_length = 20)
  trainer_number = models.CharField(max_length = 20)
  email = models.CharField(max_length = 70)
  phone_number = models.CharField(max_length = 15)
  course_teaching = models.CharField(max_length = 20)

  def __str__(self):
  	return self.first_name


# Create your models here.
