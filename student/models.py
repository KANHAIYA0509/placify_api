from django.db import models
from users.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    graduation_year = models.IntegerField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField()
    is_placed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()
