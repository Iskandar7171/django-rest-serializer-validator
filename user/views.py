from rest_framework.generics import ListCreateAPIView
from .serializer import UserFavouriteSerializer, UserCartSerializer
from .models import UserCart, UserFavourite
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class UserFavouriteListCreateApiView(ListCreateAPIView):
    queryset = UserFavourite.objects.all()
    serializer_class = UserFavouriteSerializer
    permission_classes  = [IsAuthenticated]
    
    def create(self,request):
        request.data['user'] = request.user.id
        data = super().create(request)
        print("favourite qoshildi")
        print(request.user)
        return data

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        
            
     
class UserCartListCreateApiView(ListCreateAPIView):
    queryset = UserCart.objects.all()
    serializer_class = UserCartSerializer
