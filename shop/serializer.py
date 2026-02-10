from rest_framework.serializers import ModelSerializer
from .models import Category,Product
from rest_framework.exceptions import ValidationError

class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name','is_active']
        
    def validate_name(self, value):
        print(value)
        if len(value) <=3:
            raise ValidationError("3 tadan kam bomasin")
        return (value)
        
    def is_active(self,value):
        print(value)
        if not value == False:
            raise ValidationError("bye")
        return (value)

class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
    
    def validate_name(self, value):
        print(value)
        if len(value) <=5:
            raise ValidationError("5 tadan kam bomasin!!!")
        return value
    

    def validate_is_active(self, value):
        print(value)
        if value == False:
            raise ValidationError("false bolmasin!!")
        return value

    def validate_price(self, value):
        print(value)
        if value <= 2000:
            raise ValidationError("pulingiz yetmayapti!!!!1")
        return value