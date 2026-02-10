from rest_framework.serializers import ModelSerializer
from .models import UserFavourite, UserCart

class UserFavouriteSerializer(ModelSerializer):
    
    class Meta:
        model = UserFavourite
        fields = "__all__"
        
    
class UserCartSerializer(ModelSerializer):
    
    class Meta:
        model = UserCart
        fields = "__all__"
