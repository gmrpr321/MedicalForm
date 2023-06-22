from rest_framework import serializers
from .models import StudentModel, MarkModel, ParentModel, ContactModel
from django.contrib.auth.models import User

# Application Serializers


class ApplicationMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkModel
        fields = [""]


class ApplicationParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = [
            "father_name",
            "father_occupation",
            "father_occupation_address",
            "father_phone_number",
            "father_email",
            "mother_name",
            "mother_occupation",
            "mother_occupation_address",
            "mother_email",
            "mother_phone_number",
        ]


class ApplicationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = [
            "student_contact_no",
            "student_email_id",
            "mobile_1",
            "mobile_2",
            "mobile_3",
            "guardian_mobile",
        ]


class ApplicationStudentSerializer(serializers.ModelSerializer):
    markSerializer = ApplicationMarkSerializer(many=False)
    contactSerializer = ApplicationContactSerializer(many=False)
    parentSerializer = ApplicationParentSerializer(many=False)

    class Meta:
        model = StudentModel
        fields = [
            "student_name",
            "email",
            "course",
            "quota",
            "date_of_birth",
            "gender",
            "is_hostellite",
            "community",
            "religion",
            "native_place",
            "blood_group",
            "height",
            "weight",
            "date_of_admission",
            "mother_tongue",
            "address_for_communication",
            "address_local_guardian",
        ]

    def create(self, validated_data):
        """
        data format for Application student serializer
        data = {
        email = str
        student = dict
        contact = dict
        mark = dict
        parent = dict
        }
        """
        email = validated_data.pop("email")
        student_data = validated_data.pop("student")
        contact_data = validated_data.pop("contact")
        mark_data = validated_data.pop("mark")
        parent_data = validated_data.pop("parent")

        # User will always be present for this email
        userInstance = User.objects.filter(email=email)[0]
        if userInstance:
            student = StudentModel.objects.filter(email=email).first()

            # create or update the related models of student
            final_student = None
            if student:
                for key, value in student_data.items():
                    setattr(student, key, value)

                contact_instance = student.contact_info
                mark_instance = student.mark_info
                parent_instance = student.parent_info

                for key, value in contact_data.items():
                    setattr(contact_instance, key, value)
                    contact_instance.save()

                for key, value in mark_data.items():
                    setattr(mark_instance, key, value)
                    mark_instance.save()

                for key, value in parent_data.items():
                    setattr(parent_instance, key, value)
                    parent_instance.save()

                student.save()
                final_student = student

            else:
                contact_instance = ContactModel.objects.create(**contact_data)
                parent_instance = ParentModel.objects.create(**parent_data)
                mark_instance = MarkModel.objects.create(**mark_data)
                student_instance = StudentModel.objects.create(
                    user=userInstance,
                    contact_info=contact_instance,
                    parent_info=parent_instance,
                    mark_info=mark_instance,
                    **student_data
                )
                final_student = student_instance

            return final_student


# Admission Serializers
class AdmissionMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkModel
        fields = []


class AdmissionParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = []


class AdmissionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = []


class AdmissionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = []
