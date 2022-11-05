from rest_framework.generics import GenericAPIView, mixins, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from cart import models, serializers, permission


class Cart(mixins.CreateModelMixin,
           mixins.DestroyModelMixin,
           mixins.ListModelMixin,
           GenericAPIView):

    model = models.Cart.objects
    serializer_class = serializers.CartSerializers
    permission_classes = [IsAuthenticated, permission.CurrentUserPermission]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_object(self):
        serializer = self.get_serializer(
            data=self.request.data, quantity=False)
        serializer.is_valid(raise_exception=True)
        obj = get_object_or_404(self.model, **serializer.validated_data)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return self.model.filter(user=self.request.user.id)


class CartsOfAllUsers(ListAPIView):
    queryset = models.Cart.objects
    serializer_class = serializers.CartAllFieldsSerilizers
    permission_classes = [IsAdminUser, ]
