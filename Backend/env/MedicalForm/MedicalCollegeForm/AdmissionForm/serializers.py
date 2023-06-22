from rest_framework import serializers
from .models import StudentModel, MarkModel, ParentModel, ContactModel


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
        ]


class ApplicationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = []


class ApplicationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        models = StudentModel
        fields = []


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
