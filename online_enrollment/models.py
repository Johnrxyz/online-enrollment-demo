from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

GENDERS = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
]
    
ENROLLMENT_STATUS = [
    ('P', 'Pending'),
    ('E', 'Enrolled'),
    ('D', 'Dropped')
]

DEPARTMENTS = (
    ("Bachelor of Science in Information Technology", "BSIT"),
    ("Bachelor of Science in Computer Science", "BSCS"),
    ("Bachelor of Science in Electrical Engineering", "BSEE"),
    ("Bachelor of Science in Mechanical Engineering", "BSME"),
    ("Bachelor of Science in Nursing", "BSN"),
    ("Bachelor of Arts in Communication", "BA Comm"),
    ("Bachelor of Science in Business Administration", "BSBA"),
    ("Bachelor of Arts in Psychology", "AB Psychology"),
    ("Bachelor of Science in Biology", "BS Biology"),
    ("Bachelor of Science in Civil Engineering", "BSCE"),
    ("Bachelor of Secondary Education", "BSEd"),
    ("Bachelor of Arts in English Language Studies", "ABELS")
)
class Course(models.Model):
    course_code = models.CharField(max_length=100, primary_key=True)
    course_title = models.CharField( max_length=100)
    description = models.TextField(blank=True, null=True)
    unit = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.course_title
    
class Section(models.Model):
    department = models.CharField(choices=DEPARTMENTS, default="BSIT")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_end_time = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f'SECTION ID: {self.id}, TIME: {self.start_end_time}, DAYS: {self.days_of_week}, ROOM: {self.room_number}, INSTRUCTOR: {self.instructor}'
 
class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(choices=DEPARTMENTS, default="BSIT")
    studentIdentifier = models.CharField(max_length=10, primary_key=True)
    age = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)   
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(choices=GENDERS, null=True, blank=True)
    enrollmentDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.student}'
    
#SHOULD BE ACCESSED ONLY BY TEACHERS/ADMIN
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=ENROLLMENT_STATUS, default='Pending')

    def __str__(self):
        return f'ENROLLMENT ID: {self.id}, STUDENT ID: {self.student}, DATE: {self.enrollment_date}, GRADE: {self.grade}, STATUS: {self.status}'

class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_units_earned = models.IntegerField()
    gpa = models.DecimalField(decimal_places=2, max_digits=10)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'RECORD ID: {self.id}, STUDENT ID: {self.student_id}, UNITS: {self.total_units_earned}, GPA: {self.gpa}, GRADUATIONS DATE: {self.graduation_date}'
    
class ApparelStyle(models.Model):
    """
    Represents the main clothing item style (e.g., 'Boxy Tee', 'Slim Chino Pant').
    Maps to the top-level object in the JSON array.
    """
    style_id = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="Unique identifier (e.g., boxy_tee_001)"
    )
    style_name = models.CharField(
        max_length=100, 
        verbose_name="Style Name"
    )
    description = models.TextField(
        blank=True, 
        help_text="Detailed description of the style/fit."
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Is Active/Visible"
    )

    def __str__(self):
        return self.style_name
    
    class Meta:
        verbose_name = "Apparel Style"
        verbose_name_plural = "Apparel Styles"


class SizeMeasurements(models.Model):
    """
    Represents the specific measurements for a single size within an ApparelStyle.
    This is where the flexibility comes in via the 'specs' JSONField.
    """
    apparel_style = models.ForeignKey(
        ApparelStyle, 
        on_delete=models.CASCADE, 
        related_name='measurements'
    )
    size_tag = models.CharField(
        max_length=20, 
        help_text="The displayed size label (e.g., S, M, L, 32x30)"
    )
    sku_suffix = models.CharField(
        max_length=20, 
        blank=True, 
        help_text="Suffix used for SKU generation (e.g., S, M, 3230)"
    )
    
    # --- CRITICAL FLEXIBILITY POINT ---
    # This JSONField allows us to store arbitrary measurement key-value pairs 
    # (e.g., {"length_in": 23, "width_in": 21.5} OR {"waist_in": 32, "inseam_in": 32})
    specs = models.JSONField(
        default=dict,
        verbose_name="Measurement Specifications",
        help_text="Flexible key-value pairs for measurements (e.g., length_in, waist_in)."
    )
    # -----------------------------------

    def __str__(self):
        return f"{self.apparel_style.style_name} - {self.size_tag}"
    
    class Meta:
        verbose_name = "Size Measurement"
        verbose_name_plural = "Size Measurements"
        unique_together = ('apparel_style', 'size_tag')
        ordering = ['apparel_style', 'size_tag']


# Optional: A separate model to define measurement types and units for better UI/API validation
class MeasurementUnit(models.Model):
    """
    Utility table to define known measurement keys and their units/descriptions.
    This helps an admin interface know what 'length_in' means.
    """
    key_name = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="The key used in the specs JSONField (e.g., length_in, waist_in)"
    )
    display_name = models.CharField(
        max_length=100, 
        help_text="Human-readable name (e.g., 'Garment Length', 'Waist Circumference')"
    )
    unit = models.CharField(
        max_length=10, 
        help_text="Unit of measure (e.g., in, cm)"
    )
    
    def __str__(self):
        return f"{self.display_name} ({self.unit})"
        
    class Meta:
        verbose_name = "Measurement Unit Definition"
        verbose_name_plural = "Measurement Unit Definitions"