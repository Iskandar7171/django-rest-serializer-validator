from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Post
from .serializer import PostSerializer

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        request.data['author'] = request.user.id
        data = super().create(request)
        print("Post qoshildi")
        print(request.user)
        return data

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)