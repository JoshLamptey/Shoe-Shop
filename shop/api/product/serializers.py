from .models import Product
from rest_framework import serializers

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'