from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from catalog import serializers, models


class CatalogView(ListAPIView):
    serializer_class = serializers.ProductsSerializers
    queryset = models.Products.objects
    permission_classes = [IsAuthenticated]
