from django.test import TestCase
from django.contrib.auth.models import User
from .models import StudentModel, MarkModel, ParentModel, ContactModel
from .serializers import ApplicationStudentSerializer, AdmissionStudentSerializer

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import StudentModel
from .serializers import ApplicationStudentSerializer
from .views import ApplicationFormCreate


class StudentApplicationTestCase(TestCase):
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(
            username="test@example.com",
            password="testpassword",
            email="test@example.com",
        )
        user = User.objects.create(username="testuse", email="ter", password="pasdf")

        contact = ContactModel.objects.create(mobile_1="1234567890")
        parent = ParentModel.objects.create(mother_name="oDoe")
        mark = MarkModel.objects.create()
        self.student = StudentModel.objects.create(
            email="ter",
            contact_info=contact,
            mark_info=mark,
            parent_info=parent,
            user=user,
            status=0,
        )
        self.student.save()

    def test_create_application_student_check(self):
        # Create test data
        studentData = {
            "email": "test@example.com",
            "contact_info": {
                "student_contact_no": "1234567890",
                "student_email_id": "johndoe@example.com",
                "mobile_1": "9876543210",
                "mobile_2": "",
                "mobile_3": "",
                "guardian_mobile": "9876543219",
            },
            "student_name": "John Doe",
            "course": "Engineering",
            "quota": "Govt",
            "date_of_birth": "1990-01-01",
            "gender": "Male",
            "is_hostellite": False,
            "community": "OC",
            "religion": "Christian",
            "native_place": "Chennai",
            "blood_group": "A+",
            "height": 170.5,
            "weight": 65.5,
            "date_of_admission": "2022-01-01",
            "mother_tongue": "English",
            "status": 0,
            "mark_info": {},
            "parent_info": {
                "father_name": "John Doe Sr.",
                "father_occupation": "Engineer",
                "father_occupation_address": "789 Oak St, City",
                "father_phone_number": "9876543200",
                "father_email": "johndoesr@example.com",
                "mother_name": "Jane Doe",
                "mother_occupation": "Teacher",
                "mother_occupation_address": "987 Pine St, City",
                "mother_phone_number": "9876543201",
                "mother_email": "janedoe@example.com",
            },
        }

        student_serializer = ApplicationStudentSerializer(data=studentData)
        student_serializer.is_valid()
        student_serializer.error_messages = student_serializer.errors
        print(student_serializer.error_messages)
        student_serializer.save()
        self.assertTrue(len(StudentModel.objects.all()) > 0)
        email = studentData["email"]
        mother_email = studentData["parent_info"]["mother_email"]
        db_instance = StudentModel.objects.get(email=email)
        self.assertEqual(email, db_instance.email)
        self.assertTrue(mother_email, db_instance.parent_info.mother_email)

    def test_update_application_student_check(self):
        updated_data = {
            "contact_info": {"student_contact_no": "987asdfas0dsf"},
            "parent_info": {"mother_name": "JaSmith"},
        }
        # Perform the update
        serializer = ApplicationStudentSerializer(
            instance=self.student, data=updated_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        updated_student = serializer.save()

        self.assertEqual(
            updated_data["contact_info"]["student_contact_no"],
            updated_student.contact_info.student_contact_no,
        )
        self.assertEqual(
            updated_data["parent_info"]["mother_name"],
            updated_student.parent_info.mother_name,
        )


class StudentAdmissionTestCase(TestCase):
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(
            username="te", password="testpassword", email="test@examp.com"
        )
        user = User.objects.create(
            username="tedf", email="tesexam.com", password="pasdf"
        )

        contact = ContactModel.objects.create(mobile_1="1234567890")
        parent = ParentModel.objects.create(mother_name="oDoe")
        mark = MarkModel.objects.create()
        self.student = StudentModel.objects.create(
            email="te",
            contact_info=contact,
            mark_info=mark,
            parent_info=parent,
            user=user,
            status=0,
        )
        self.student.save()

    def test_create_admission_student_check(self):
        # Create test data
        studentData = {
            "email": "test@examp.com",
            "contact_info": {
                "student_contact_no": "1234567890",
                "student_email_id": "johndoe@example.com",
                "mobile_1": "9876543210",
                "mobile_2": "",
                "mobile_3": "",
                "guardian_mobile": "9876543219",
            },
            "student_name": "John Doe",
            "course": "Engineering",
            "quota": "Govt",
            "date_of_birth": "1990-01-01",
            "gender": "Male",
            "is_hostellite": False,
            "community": "OC",
            "religion": "Christian",
            "native_place": "Chennai",
            "blood_group": "A+",
            "height": 170.5,
            "weight": 65.5,
            "date_of_admission": "2022-01-01",
            "mother_tongue": "English",
            "status": 0,
            "mark_info": {
                "neet_roll_no": "NEET123",
                "hsc_year_of_passing": 2022,
                "neet_year": 2022,
                "neet_study_center_name": "XYZ Study Center",
                "no_of_neet_attempts": 2,
                "board_of_study": "CBSE",
                "neet_air": 100,
                "selection_committee_allotment_order_no": "ALLOT123",
                "selection_committee_general_rank": "RANK123",
                "allotment_order_data": "2022-06-30",
                "neet_physics_mark": 120,
                "neet_chemistry_mark": 130,
                "neet_biology_mark": 140,
                "neet_total_mark": 390,
                "neet_physics_percentile": 90.5,
                "neet_chemistry_percentile": 85.2,
                "neet_biology_percentile": 92.3,
                "neet_total_percentile": 88.7,
                "hsc_physics_mark": 95.5,
                "hsc_chemistry_mark": 93.8,
                "hsc_biology_mark": 96.2,
                "hsc_total_mark": 285.5,
                "hsc_marks_maximum": 300,
                "pcb_percentage": 95.17,
            },
            "parent_info": {
                "father_name": "John Doe Sr.",
                "father_occupation": "Engineer",
                "father_occupation_address": "789 Oak St, City",
                "father_phone_number": "9876543200",
                "father_email": "johndoesr@example.com",
                "mother_name": "Jane Doe",
                "mother_occupation": "Teacher",
                "mother_occupation_address": "987 Pine St, City",
                "mother_phone_number": "9876543201",
                "mother_email": "janedoe@example.com",
            },
        }

        student_serializer = AdmissionStudentSerializer(data=studentData)
        student_serializer.is_valid()
        student_serializer.error_messages = student_serializer.errors
        print(student_serializer.error_messages)
        student_serializer.save()
        self.assertTrue(len(StudentModel.objects.all()) > 0)
        email = studentData["email"]
        mother_email = studentData["parent_info"]["mother_email"]
        db_instance = StudentModel.objects.get(email=email)
        self.assertEqual(email, db_instance.email)
        self.assertTrue(mother_email, db_instance.parent_info.mother_email)

    def test_update_admission_student_check(self):
        updated_data = {
            "contact_info": {"student_contact_no": "987asdfas0"},
            "parent_info": {"mother_name": "JaSmith"},
        }
        # Perform the update
        serializer = AdmissionStudentSerializer(
            instance=self.student, data=updated_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        updated_student = serializer.save()

        self.assertEqual(
            updated_data["contact_info"]["student_contact_no"],
            updated_student.contact_info.student_contact_no,
        )
        self.assertEqual(
            updated_data["parent_info"]["mother_name"],
            updated_student.parent_info.mother_name,
        )


# Testing views
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import StudentModel
from .serializers import ApplicationStudentSerializer
from .views import ApplicationFormCreate


class ApplicationFormTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("application-create")
        self.user = User.objects.create_user(
            username="test@example.com",
            password="testpassword",
            email="test@example.com",
        )
        self.valid_payload = {
            "email": "test@example.com",
            "contact_info": {
                "student_contact_no": "1234567890",
                "student_email_id": "johndoe@example.com",
                "mobile_1": "9876543210",
                "mobile_2": "",
                "mobile_3": "",
                "guardian_mobile": "9876543219",
            },
            "student_name": "John Doe",
            "course": "Engineering",
            "quota": "Govt",
            "date_of_birth": "1990-01-01",
            "gender": "Male",
            "is_hostellite": False,
            "community": "OC",
            "religion": "Christian",
            "native_place": "Chennai",
            "blood_group": "A+",
            "height": 170.5,
            "weight": 65.5,
            "date_of_admission": "2022-01-01",
            "mother_tongue": "English",
            "status": 0,
            "mark_info": {},
            "parent_info": {
                "father_name": "John Doe Sr.",
                "father_occupation": "Engineer",
                "father_occupation_address": "789 Oak St, City",
                "father_phone_number": "9876543200",
                "father_email": "johndoesr@example.com",
                "mother_name": "Jane Doe",
                "mother_occupation": "Teacher",
                "mother_occupation_address": "987 Pine St, City",
                "mother_phone_number": "9876543201",
                "mother_email": "janedoe@example.com",
            },
        }
        user = User.objects.create(username="testuse", email="ter", password="pasdf")

        contact = ContactModel.objects.create(mobile_1="1234567890")
        parent = ParentModel.objects.create(mother_name="oDoe")
        mark = MarkModel.objects.create()
        self.student = StudentModel.objects.create(
            email="ter",
            contact_info=contact,
            mark_info=mark,
            parent_info=parent,
            user=user,
            status=0,
        )
        self.student.save()

    def test_create_application_form(self):
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the created object in the database
        created_object = StudentModel.objects.get(email=self.valid_payload["email"])
        serializer = ApplicationStudentSerializer(created_object)
        self.assertEqual(response.data, serializer.data)

    def test_update_application_form(self):
        url = reverse("application-update", kwargs={"pk": self.student.email})
        patch_data = {
            "email": "ter",
            "contact_info": {"student_contact_no": "9876543210"},
            "parent_info": {"mother_name": "Jane Smith"},
            "mark_info": {},
            "status": -1,
        }
        response = self.client.put(url, patch_data, format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print(response.data)  # Print serializer errors

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_application_retrive(self):
        url = reverse("application-retrive", kwargs={"pk": self.student.pk})
        response = self.client.get(url)
        print(response.data)


# ADMISSION TEST CASE


class AdmissionFormTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("admission-create")
        self.user = User.objects.create_user(
            username="test@examp.com",
            password="testpassword",
            email="test@examp.com",
        )
        self.valid_payload = {
            "email": "test@examp.com",
            "contact_info": {
                "student_contact_no": "1234567890",
                "student_email_id": "johndoe@example.com",
                "mobile_1": "9876543210",
                "mobile_2": "",
                "mobile_3": "",
                "guardian_mobile": "9876543219",
            },
            "student_name": "John Doe",
            "course": "Engineering",
            "quota": "Govt",
            "date_of_birth": "1990-01-01",
            "gender": "Male",
            "is_hostellite": False,
            "community": "OC",
            "religion": "Christian",
            "native_place": "Chennai",
            "blood_group": "A+",
            "height": 170.5,
            "weight": 65.5,
            "date_of_admission": "2022-01-01",
            "mother_tongue": "English",
            "status": 0,
            "mark_info": {
                "neet_roll_no": "NEET123",
                "hsc_year_of_passing": 2022,
                "neet_year": 2022,
                "neet_study_center_name": "XYZ Study Center",
                "no_of_neet_attempts": 2,
                "board_of_study": "CBSE",
                "neet_air": 100,
                "selection_committee_allotment_order_no": "ALLOT123",
                "selection_committee_general_rank": "RANK123",
                "allotment_order_data": "2022-06-30",
                "neet_physics_mark": 120,
                "neet_chemistry_mark": 130,
                "neet_biology_mark": 140,
                "neet_total_mark": 390,
                "neet_physics_percentile": 90.5,
                "neet_chemistry_percentile": 85.2,
                "neet_biology_percentile": 92.3,
                "neet_total_percentile": 88.7,
                "hsc_physics_mark": 95.5,
                "hsc_chemistry_mark": 93.8,
                "hsc_biology_mark": 96.2,
                "hsc_total_mark": 285.5,
                "hsc_marks_maximum": 300,
                "pcb_percentage": 95.17,
            },
            "parent_info": {
                "father_name": "John Doe Sr.",
                "father_occupation": "Engineer",
                "father_occupation_address": "789 Oak St, City",
                "father_phone_number": "9876543200",
                "father_email": "johndoesr@example.com",
                "mother_name": "Jane Doe",
                "mother_occupation": "Teacher",
                "mother_occupation_address": "987 Pine St, City",
                "mother_phone_number": "9876543201",
                "mother_email": "janedoe@example.com",
            },
        }
        user = User.objects.create(username="testuse", email="ter", password="pasdf")

        contact = ContactModel.objects.create(mobile_1="1234567890")
        parent = ParentModel.objects.create(mother_name="oDoe")
        mark = MarkModel.objects.create()
        self.student = StudentModel.objects.create(
            email="ter",
            contact_info=contact,
            mark_info=mark,
            parent_info=parent,
            user=user,
            status=0,
        )
        self.student.save()

    def test_create_admission_form(self):
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the created object in the database
        created_object = StudentModel.objects.get(email=self.valid_payload["email"])
        serializer = AdmissionStudentSerializer(created_object)
        self.assertEqual(response.data, serializer.data)

    def test_update_admission_form(self):
        url = reverse("admission-update", kwargs={"pk": self.student.email})
        patch_data = {
            "email": "ter",
            "contact_info": {"student_contact_no": "9876543210"},
            "parent_info": {"mother_name": "Jane"},
            "mark_info": {},
            "status": -1,
        }
        response = self.client.put(url, patch_data, follow=True, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        db_instance = StudentModel.objects.filter(
            parent_info__mother_name=patch_data["parent_info"]["mother_name"]
        )
        self.assertTrue(len(db_instance) > 0)

    def test_admission_retrive(self):
        url = reverse("admission-retrive", kwargs={"pk": self.student.pk})
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
