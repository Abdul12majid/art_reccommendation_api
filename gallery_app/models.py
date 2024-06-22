from django.db import models

# Create your models here.
class Art_Work(models.Model):
	artiste = models.CharField(max_length=60, null=True, blank=False)
	art_title = models.CharField(max_length=60, blank=False)
	art_image = models.ImageField(blank=True, upload_to="art_images/")
	art_desc = models.TextField(blank=True)

	def __str__(self):
		return f'{self.artiste} {self.art_title}'

