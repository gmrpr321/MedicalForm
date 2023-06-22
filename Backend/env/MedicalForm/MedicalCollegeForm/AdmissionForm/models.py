from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    serial_no = models.CharField(max_length=500, primary_key=True)
    date_of_joining = models.DateField()
    admission_no = models.CharField(max_length=500)
    ar_number = models.CharField(max_length=200)
    allotment_date = models.DateField()
    student_name = models.CharField(max_length=500)
    university_register_number = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    is_hostellite = models.BooleanField()
    community = models.CharField(max_length=20, choices=community_choices)
    religion = models.CharField(max_length=300)
    caste = models.CharField(max_length=300)
    hsc_school_name = models.CharField(max_length=500)
    hsc_register_no = models.CharField(max_length=100)
    medium_of_study = models.CharField(max_length=200)
    native_place = models.CharField(max_length=500)
    blood_group = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    address_for_communication = models.CharField(max_length=5000)
    address_local_guardian = models.CharField(max_length=5000)
    neet_hall_ticket_no = models.CharField(max_length=300)
    neet_roll_no = models.CharField(max_length=300)
    nationality = models.CharField(max_length=200)
    quota = models.CharField(max_length=20, choices=quota_choices)
    scholarship = models.CharField(max_length=500)
    general_rank = models.IntegerField(validators=[MinValueValidator(0)])
    mother_tongue = models.CharField(max_length=300)
    # FOREIGN KEYS
    contact_info = models.OneToOneField(
        "AdmissionForm.ContactModel", on_delete=models.CASCADE
    )
    parent_info = models.OneToOneField(
        "AdmissionForm.ParentModel", on_delete=models.CASCADE
    )
    mark_info = models.OneToOneField(
        "AdmissionForm.ParentModel", on_delete=models.CASCADE
    )


class ContactModel(models.Model):
    student_contact_no = models.CharField(max_length=50)
    student_email_id = models.EmailField(max_length=200)
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20)
    mobile_3 = models.CharField(max_length=20)
    guardian_mobile = models.CharField(max_length=20)


class ParentModel(models.Model):
    father_name = models.CharField(max_length=500)
    father_occupation = models.CharField(max_length=500)
    father_occupation_address = models.CharField(max_length=500)
    father_phone_number = models.CharField(max_length=20)
    father_email = models.EmailField(max_length=200)
    mother_name = models.CharField(max_length=500)
    mother_occupation = models.CharField(max_length=500)
    mother_occupation_address = models.CharField(max_length=500)
    mother_phone_number = models.CharField(max_length=20)
    mother_email = models.EmailField(max_length=200)


class MarkModel(models.Model):
    board_choices = [
        ("State", "State"),
        ("CBSE", "CBSE"),
        ("ICSE", "ICSE"),
        ("Others", "Others"),
    ]
    neet_roll_no = models.CharField(max_length=200)
    hsc_year_of_passing = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)]
    )
    neet_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)]
    )
    neet_study_center_name = models.CharField(max_digits=500, blank=True)
    no_of_neet_attempts = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    neet_air = models.IntegerField(validators=[MinValueValidator(0)])
    selection_committee_allotment_order_no = models.CharField(max_length=500)
    selection_committee_general_rank = models.CharField(max_length=500)
    allotment_order_data = models.DateField()
    # NEET MARKS
    neet_physics_mark = models.IntegerField(validators=[MinValueValidator(0)])
    neet_chemistry_mark = models.IntegerField(validators=[MinValueValidator(0)])
    neet_biology_mark = models.IntegerField(validators=[MinValueValidator(0)])
    neet_total_mark = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(720)]
    )
    # NEET PERCENTILE
    neet_physics_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    neet_chemistry_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    neet_biology_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    neet_total_neet_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    # HSC MARKS
    hsc_physics_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
    )
    hsc_chemistry_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
    )
    hsc_biology_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
    )
    hsc_total_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
    )
    hsc_marks_maximum = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
    )
    pcb_percentage = models.DecimalField(
        max_digits=7, decimal_places=4, validators=[MinValueValidator(0)]
    )
