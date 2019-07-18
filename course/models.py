from django.db import models


from trainer.models import Trainer
trainer = models.ForeignKey(Trainer,null=True,on_delete=models.CASCADE)

class Course(models.Model):
	name = models.CharField(max_length = 25)
	duration_in_months = models.IntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()

	def __str__(self):
		return self.name


# Create your models here.
