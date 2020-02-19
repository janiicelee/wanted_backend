from django.db import models
from user.models import User
from job.models import SubCategory

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.SET_NULL, null = True)
    education = models.CharField(max_length = 1000, null=True)
    language = models.CharField(max_length = 500, null=True)
    link = models.URLField(max_length = 1000, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'resumes'

class Career(models.Model):
    name = models.CharField(max_length = 50, null=True)
    company = models.CharField(max_length = 30, null=True)
    description = models.TextField(max_length = 5000, null=True)
    resume = models.ForeignKey(Resume, on_delete = models.SET_NULL, null=True)
    started_at = models.DateField(null=True)
    ended_at = models.DateField(null=True)

    class Meta:
        db_table = 'careers'