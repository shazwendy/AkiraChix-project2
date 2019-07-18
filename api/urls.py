from django.urls import path,include
from .views import StudentViewSet
from rest_framework import routers


# from django.urls import path,include
from .views import TrainerViewSet
from .views import CourseViewSet
# from rest_framework import routers

router = routers.DefaultRouter()
router.register("students", StudentViewSet)

router.register("trainers", TrainerViewSet)

router.register("courses", CourseViewSet)

urlpatterns = [
path("", include(router.urls)),]