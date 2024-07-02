from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class A_or_U(models.Model):
	name = models.CharField(max_length=200, blank=False)

	class Meta:
		verbose_name_plural = 'Status'

	def __str__(self):
		return f'{self.name}'

class Profile(models.Model):
	user=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	status = models.ForeignKey(A_or_U, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username}'

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile = Profile(user=instance)
		profile.save()

post_save.connect(create_profile, sender=User)