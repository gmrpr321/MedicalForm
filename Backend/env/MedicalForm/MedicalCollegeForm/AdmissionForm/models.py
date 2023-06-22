from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class ContactModel(models.Model):
    student_contact_no = models.CharField(max_length=50, default="")
    student_email_id = models.EmailField(max_length=200, default="")
    mobile_1 = models.CharField(max_length=20, default="")
    mobile_2 = models.CharField(max_length=20, default="")
    mobile_3 = models.CharField(max_length=20, default="")
    guardian_mobile = models.CharField(max_length=20, default="")


class ParentModel(models.Model):
    father_name = models.CharField(max_length=500, default="")
    father_occupation = models.CharField(max_length=500, default="")
    father_occupation_address = models.CharField(max_length=500, default="")
    father_phone_number = models.CharField(max_length=20, default="")
    father_email = models.EmailField(max_length=200, default="")
    mother_name = models.CharField(max_length=500, default="")
    mother_occupation = models.CharField(max_length=500, default="")
    mother_occupation_address = models.CharField(max_length=500, default="")
    mother_phone_number = models.CharField(max_length=20, default="")
    mother_email = models.EmailField(max_length=200, default="")


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class MarkModel(models.Model):
    board_choices = [
        ("State", "State"),
        ("CBSE", "CBSE"),
        ("ICSE", "ICSE"),
        ("Others", "Others"),
    ]
    neet_roll_no = models.CharField(max_length=200, default="")
    hsc_year_of_passing = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)], default=0
    )
    neet_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)], default=0
    )
    neet_study_center_name = models.CharField(max_length=500, blank=True, default="")
    no_of_neet_attempts = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=0
    )
    board_of_study = models.CharField(max_length=30, choices=board_choices, default="")
    neet_air = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    selection_committee_allotment_order_no = models.CharField(
        max_length=500, default=""
    )
    selection_committee_general_rank = models.CharField(max_length=500, default="")
    allotment_order_data = models.DateField(default=None, null=True)
    # NEET MARKS
    neet_physics_mark = models.IntegerField(
        validators=[MinValueValidator(0)], default=0
    )
    neet_chemistry_mark = models.IntegerField(
        validators=[MinValueValidator(0)], default=0
    )
    neet_biology_mark = models.IntegerField(
        validators=[MinValueValidator(0)], default=0
    )
    neet_total_mark = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(720)], default=0
    )
    # NEET PERCENTILE
    neet_physics_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
    )
    neet_chemistry_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
    )
    neet_biology_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
    )
    neet_total_neet_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
    )
    # HSC MARKS
    hsc_physics_mark = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)], default=0.0
    )
    hsc_chemistry_mark = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)], default=0.0
    )
    hsc_biology_mark = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)], default=0.0
    )
    hsc_total_mark = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)], default=0.0
    )
    hsc_marks_maximum = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)], default=0.0
    )
    pcb_percentage = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)], default=0.0
    )


class StudentModel(models.Model):
    quota_choices = [
        ("Govt", "Govt"),
        ("Mgt", "Mgt"),
        ("NRI", "NRI"),
        ("NRILapsed", "NRILapsed"),
    ]
    community_choices = [
        ("OC", "OC"),
        ("BC", "BC"),
        ("MBC", "MBc"),
        ("SC", "SC"),
        ("SCA", "SCA"),
        ("ST", "ST"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    serial_no = models.CharField(max_length=500, default="")
    email = models.CharField(max_length=500, primary_key=True)
    date_of_joining = models.DateField(default=None, null=True)
    admission_no = models.CharField(max_length=500, default="")
    ar_number = models.CharField(max_length=200, default="")
    allotment_date = models.DateField(default=None, null=True)
    student_name = models.CharField(max_length=500, default="")
    course = models.CharField(max_length=200, default="")
    university_register_number = models.CharField(max_length=100, default="")
    date_of_birth = models.DateField(default=None, null=True)
    gender = models.CharField(max_length=100, default="")
    is_hostellite = models.BooleanField(default=False)
    community = models.CharField(max_length=20, choices=community_choices, default="")
    religion = models.CharField(max_length=300, default="")
    caste = models.CharField(max_length=300, default="")
    hsc_school_name = models.CharField(max_length=500, default="")
    hsc_register_no = models.CharField(max_length=100, default="")
    medium_of_study = models.CharField(max_length=200, default="")
    native_place = models.CharField(max_length=500, default="")
    blood_group = models.CharField(max_length=30, default="")
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    address_for_communication = models.CharField(max_length=5000, default="")
    address_local_guardian = models.CharField(max_length=5000, default="")
    neet_hall_ticket_no = models.CharField(max_length=300, default="")
    neet_roll_no = models.CharField(max_length=300, default="")
    nationality = models.CharField(max_length=200, default="")
    quota = models.CharField(max_length=20, choices=quota_choices, default="")
    scholarship = models.CharField(max_length=500, default="")
    general_rank = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    mother_tongue = models.CharField(max_length=300, default="")
    # FOREIGN KEYS
    contact_info = models.OneToOneField(
        ContactModel, on_delete=models.CASCADE, default=None, null=True
    )
    parent_info = models.OneToOneField(
        ParentModel, on_delete=models.CASCADE, default=None, null=True
    )
    mark_info = models.OneToOneField(
        MarkModel, on_delete=models.CASCADE, default=None, null=True
    )
