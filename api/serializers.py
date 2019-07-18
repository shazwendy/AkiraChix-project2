from student.models import Student
from trainer.models import Trainer
from course.models import Course
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"




class TrainerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Trainer
		fields = "__all__"




class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = "__all__"