from django.db import models

class User(models.Model):
	user       = models.CharField(max_length = 50)
	email      = models.CharField(max_length = 200, unique = True)
	password   = models.CharField(max_length = 300, null=True)
	created_at = models.DateTimeField(auto_now_add  = True)
	updated_at = models.DateTimeField(auto_now= True)

	class Meta:
		db_table = 'users'


