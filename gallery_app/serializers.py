from rest_framework import serializers
from .models import Art_Work

class Art_Work_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Art_Work
		fields = ('id', 'artiste', 'art_title', 'art_image',)