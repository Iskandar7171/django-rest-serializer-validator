from rest_framework.serializers import ModelSerializer
from .models import Mijoz
from rest_framework.exceptions import ValidationError

class MijozSerizalizer(ModelSerializer):
    
    class Meta:
        model = Mijoz
        fields = "__all__"
        
    def validate_ism(self,value):
        print(value)
        if len(value) <= 5:
            raise ValidationError("5 tadan kam bo'lmasin")
        return(value)
    
    def validate_raqam(self, value):
        if not str(value).startswith("998"):
            raise ValidationError("Raqam 998 bilan boshlansin")
        return value
    
    def validate_raqam2(self, value):
        if not str(value).startswith("998"):
            raise ValidationError("Raqam 998 bilan boshlansin")
        return value
            
    def validate_yosh(self,value):
        print(value)
        if value < 18: 
            raise ValidationError("yoshi 18 dan kam bo'lmasin")
        return value
    
    def validate_address(self, value):
        print(value)
        if not (15 < len(value) < 30):
            raise ValueError("Manzil uzunligi 15 dan kotta va 30 kam bosin")
        return value
    
    def validate_dokon_nomi(self, value):
        print(value)
        if 'a' not in value.lower():
            raise ValueError("Do'kon nomi ichida a bosin")
        return value