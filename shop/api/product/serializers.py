from .models import Product
from rest_framework import serializers

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = Product
        fields = '__all__'