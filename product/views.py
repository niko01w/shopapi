from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Product
from . import serializers
from .permissions import IsAuthor
from rating.serializers import ReviewSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()


    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializers
        return serializers.ProductDetailSerializer

    def get_permissions(self):
        if self.action in('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #api/v1/product/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        product = self.get_object()
        if request.method == 'GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if product.reviews.filter(owner=request.user).exists():
            return response.Response("вы уже оставляли отзыв!!", status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, product=product)
        return response.Response(serializers.data, status=201)