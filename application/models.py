from django.db import models

# Create your models here.
from django.db import models
from student.models import StudentProfile
from company.models import JobPost

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('offered', 'Offered'),
        ('accepted', 'Accepted'),
    ]

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'job_post')  # one application per job per student

    def __str__(self):
        return f"{self.student.user.get_full_name()} -> {self.job_post.title} ({self.status})"
