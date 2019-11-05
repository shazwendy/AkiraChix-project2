from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime



class StudentCourseTestCase(TestCase):
    def setUp(self):
        self.student_a = Student.objects.create (
            first_name = "Sharon",
            last_name = "Akoth",
            date_of_birth = datetime.date(1997,11,12),
            gender = "female",
            registration_number = "123",
            email = "akothsharon19@gmail.com",
            phone_number = "072574757",
            date_joined = datetime.date.today(),
            )

        self.student_b = Student.objects.create (
            first_name = "Naima",
            last_name = "Hassan",
            date_of_birth = datetime.date(2019,4,12),
            gender = "female",
            registration_number = "A200",
            email = "akothsharon19@gmail.com",
            phone_number = "072574757",
            date_joined = datetime.date.today(),
            )

        self.course = Course.objects.create (
            name = "python",
            duration_in_months = 10,
            start_date = datetime.date.today(),
            end_date = datetime.date.today(),
            description = "Programming language. I enjoy using Django and coming up with new projects",
            )

        self.course = Course.objects.create (
            name = "entrepreneurship",
            duration_in_months = 10,
            start_date = datetime.date.today(),
            end_date = datetime.date.today(),
            description = " It's about coming up with business ideas, knowing how to work with your idea to get your product-market-fit and knowing and understanding one's target market. Business skills come in handy too.",
            )

        self.course = Course.objects.create (
            name = "graphic_design",
            duration_in_months = 10,
            start_date = datetime.date.today(),
            end_date = datetime.date.today(),
            description = " This is where one's creativity comes to action. Coming up with logos, using photoshop, working on Adobe illustrator, using InDesign and many more. It's the most exciting and interesting course for me",
            )

    # def test_student_can_join_a_course(self):
        # self.student_a.courses.add(self.Python)
        # self.assertEqual(selfstudent_a.courses.count(),1)
        # self.student_a.courses.add(self.Entrepreneurship)
        # self.assertEqual(selfstudent_a.courses.count(),2)

    def test_student_can_join_many_courses(self):
        self.student_b.courses.add(self.python, self.entrepreneurship, self.graphic_design)
        self.assertEqual(self.student.b.courses.count(), 3)

