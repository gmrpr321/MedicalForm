from rest_framework import serializers
from .models import StudentModel, MarkModel, ParentModel, ContactModel
from django.contrib.auth.models import User

# Application Serializers


class ApplicationMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkModel
        fields = "__all__"


class ApplicationParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = "__all__"


class ApplicationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"


class ApplicationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.username

    parent_info = ApplicationParentSerializer(many=False)
    mark_info = ApplicationMarkSerializer(many=False)
    contact_info = ApplicationContactSerializer(many=False)
    user = serializers.SerializerMethodField()

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
        contact_data = validated_data.pop("contact_info")
        mark_data = validated_data.pop("mark_info")
        parent_data = validated_data.pop("parent_info")

        contact_instance = ContactModel.objects.create(**contact_data)
        mark_instance = MarkModel.objects.create(**mark_data)
        parent_instance = ParentModel.objects.create(**parent_data)
        user_instance = User.objects.get(email=email)
        student_instance = StudentModel.objects.create(
            email=email,
            contact_info=contact_instance,
            mark_info=mark_instance,
            parent_info=parent_instance,
            user=user_instance,
            **validated_data
        )

        return student_instance

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact_info", {})
        mark_data = validated_data.pop("mark_info", {})
        parent_data = validated_data.pop("parent_info", {})

        contact_instance = instance.contact_info
        if contact_data:
            for key, value in contact_data.items():
                setattr(contact_instance, key, value)
            contact_instance.save()

        mark_instance = instance.mark_info
        if mark_data:
            for key, value in mark_data.items():
                setattr(mark_instance, key, value)
            mark_instance.save()

        parent_instance = instance.parent_info
        if parent_data:
            for key, value in parent_data.items():
                setattr(parent_instance, key, value)
            parent_instance.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


# Admission Serializers
class AdmissionMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkModel
        fields = "__all__"


class AdmissionParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = "__all__"


class AdmissionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"


class AdmissionStudentSerializer(serializers.ModelSerializer):
    mark_info = AdmissionMarkSerializer(many=False)
    parent_info = AdmissionParentSerializer(many=False)
    contact_info = AdmissionContactSerializer(many=False)
    user = serializers.SerializerMethodField()

    class Meta:
        model = StudentModel
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.username

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
        contact_data = validated_data.pop("contact_info")
        mark_data = validated_data.pop("mark_info")
        parent_data = validated_data.pop("parent_info")

        contact_instance = ContactModel.objects.create(**contact_data)
        mark_instance = MarkModel.objects.create(**mark_data)
        parent_instance = ParentModel.objects.create(**parent_data)
        user_instance = User.objects.get(email=email)
        student_instance = StudentModel.objects.create(
            email=email,
            contact_info=contact_instance,
            mark_info=mark_instance,
            parent_info=parent_instance,
            user=user_instance,
            **validated_data
        )
        return student_instance

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact_info", {})
        mark_data = validated_data.pop("mark_info", {})
        parent_data = validated_data.pop("parent_info", {})

        contact_instance = instance.contact_info
        if contact_data:
            for key, value in contact_data.items():
                setattr(contact_instance, key, value)
            contact_instance.save()

        mark_instance = instance.mark_info
        if mark_data:
            for key, value in mark_data.items():
                setattr(mark_instance, key, value)
            mark_instance.save()

        parent_instance = instance.parent_info
        if parent_data:
            for key, value in parent_data.items():
                setattr(parent_instance, key, value)
            parent_instance.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
