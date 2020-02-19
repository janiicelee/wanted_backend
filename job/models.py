from django.db import models
from user.models import User

class JobPosting(models.Model):
    company = models.ForeignKey('Company', on_delete = models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
    sub_category = models.ForeignKey('SubCategory', on_delete = models.SET_NULL, null=True)
    image = models.URLField(max_length = 2000, null = True)
    details = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    like = models.ManyToManyField(User, through = 'JobUser')
    
    class Meta:
        db_table = 'job_postings'

class Company(models.Model):
    name = models.CharField(max_length = 30, null=True)
    image = models.URLField(max_length = 500, null= True)
    details = models.TextField(max_length = 2000, null=True)
    salary = models.IntegerField(null = True)
    staff = models.IntegerField(null=True)
    address = models.CharField(max_length = 1000, null=True)
    lat = models.DecimalField(max_digits = 13, decimal_places = 10 , null = True)
    lng = models.DecimalField(max_digits = 13, decimal_places = 10, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    follow = models.ManyToManyField(User, through = 'CompanyUser')
    tag = models.ManyToManyField('Tag', through = 'CompanyTag')


    class Meta:
        db_table = 'companies'

class CompanyTag(models.Model):
    company = models.ForeignKey(Company, on_delete = models.SET_NULL, null=True)
    tag = models.ForeignKey('Tag', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'company_tags'

class Category(models.Model):
    title = models.CharField(max_length = 50, null=True)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    title = models.CharField(max_length = 50, null=True)
    

    class Meta:
        db_table = 'subcategories'

class JobUser(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete= models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)

    class Meta:
        db_table = 'job_users'

class Tag(models.Model):
    title = models.CharField(max_length =50, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'tags'

class CompanyUser(models.Model):
    company = models.ForeignKey(Company, on_delete = models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'company_users'


