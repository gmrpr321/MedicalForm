from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class ContactModel(models.Model):
    student_contact_no = models.CharField(max_length=50, default="", blank=True)
    student_email_id = models.EmailField(max_length=200, default="", blank=True)
    mobile_1 = models.CharField(max_length=20, default="", blank=True)
    mobile_2 = models.CharField(max_length=20, default="", blank=True)
    mobile_3 = models.CharField(max_length=20, default="", blank=True)
    guardian_mobile = models.CharField(max_length=20, default="", blank=True)


class ParentModel(models.Model):
    father_name = models.CharField(max_length=500, default="", blank=True)
    father_occupation = models.CharField(max_length=500, default="", blank=True)
    father_occupation_address = models.CharField(max_length=500, default="", blank=True)
    father_phone_number = models.CharField(max_length=20, default="", blank=True)
    father_email = models.EmailField(max_length=200, default="", blank=True)
    mother_name = models.CharField(max_length=500, default="", blank=True)
    mother_occupation = models.CharField(max_length=500, default="", blank=True)
    mother_occupation_address = models.CharField(max_length=500, default="", blank=True)
    mother_phone_number = models.CharField(max_length=20, default="", blank=True)
    mother_email = models.EmailField(max_length=200, default="", blank=True)


class MarkModel(models.Model):
    board_choices = [
        ("State", "State"),
        ("CBSE", "CBSE"),
        ("ICSE", "ICSE"),
        ("Others", "Others"),
    ]
    neet_roll_no = models.CharField(max_length=200, default="", blank=True)
    hsc_year_of_passing = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)],
        default=0,
        blank=True,
    )
    neet_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)],
        default=0,
        blank=True,
    )
    neet_study_center_name = models.CharField(max_length=500, blank=True, default="")
    no_of_neet_attempts = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=0, blank=True
    )
    board_of_study = models.CharField(
        max_length=30, choices=board_choices, default="", blank=True
    )
    neet_air = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    selection_committee_allotment_order_no = models.CharField(
        max_length=500, default="", blank=True
    )
    selection_committee_general_rank = models.CharField(
        max_length=500, default="", blank=True
    )
    allotment_order_data = models.DateField(default=None, null=True, blank=True)
    # NEET MARKS
    neet_physics_mark = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    neet_chemistry_mark = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    neet_biology_mark = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    neet_total_mark = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(720)], default=0, blank=True
    )
    # NEET PERCENTILE
    neet_physics_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    neet_chemistry_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    neet_biology_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    neet_total_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    # HSC MARKS
    hsc_physics_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_chemistry_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_biology_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_total_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_marks_maximum = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    pcb_percentage = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
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
    serial_no = models.CharField(max_length=500, default="", blank=True)
    email = models.CharField(max_length=500, primary_key=True, blank=True)
    date_of_joining = models.DateField(default=None, null=True, blank=True)
    date_of_admission = models.DateField(default=None, null=True, blank=True)
    admission_no = models.CharField(max_length=500, default="", blank=True)
    ar_number = models.CharField(max_length=200, default="", blank=True)
    allotment_date = models.DateField(default=None, null=True, blank=True)
    student_name = models.CharField(max_length=500, default="", blank=True)
    course = models.CharField(max_length=200, default="", blank=True)
    university_register_number = models.CharField(
        max_length=100, default="", blank=True
    )
    date_of_birth = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=100, default="", blank=True)
    is_hostellite = models.BooleanField(default=False, blank=True)
    community = models.CharField(
        max_length=20, choices=community_choices, default="", blank=True
    )
    religion = models.CharField(max_length=300, default="", blank=True)
    caste = models.CharField(max_length=300, default="", blank=True)
    hsc_school_name = models.CharField(max_length=500, default="", blank=True)
    hsc_register_no = models.CharField(max_length=100, default="", blank=True)
    medium_of_study = models.CharField(max_length=200, default="", blank=True)
    native_place = models.CharField(max_length=500, default="", blank=True)
    blood_group = models.CharField(max_length=30, default="", blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, blank=True
    )
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, blank=True
    )
    address_for_communication = models.CharField(
        max_length=5000, default="", blank=True
    )
    address_local_guardian = models.CharField(max_length=5000, default="", blank=True)
    neet_hall_ticket_no = models.CharField(max_length=300, default="", blank=True)
    neet_roll_no = models.CharField(max_length=300, default="", blank=True)
    nationality = models.CharField(max_length=200, default="", blank=True)
    quota = models.CharField(
        max_length=20, choices=quota_choices, default="", blank=True
    )
    scholarship = models.CharField(max_length=500, default="", blank=True)
    general_rank = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    mother_tongue = models.CharField(max_length=300, default="", blank=True)
    # APPLICATION STATUS
    status = models.IntegerField(
        validators=[MinValueValidator(-1), MaxValueValidator(1)]
    )
    # FOREIGN KEYS
    contact_info = models.OneToOneField(
        ContactModel, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    parent_info = models.OneToOneField(
        ParentModel, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    mark_info = models.OneToOneField(
        MarkModel, on_delete=models.CASCADE, default=None, null=True, blank=True
    )

    def __str__(self):
        return self.email
