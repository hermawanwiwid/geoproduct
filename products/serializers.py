from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		# fields = ('title','pub_date')
		fields = '__all__'
		