from rest_framework import generics, permissions, status
from menu.models import MenuItem, PurchaseHistory
from menu.serializers import MenuItemSerializer, PurchaseHistorySerializer
from rest_framework.response import Response
from .serializers import PurchaseHistorySerializer, BulkPurchaseHistorySerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class PurchaseHistoryListCreate(generics.ListCreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer

    def create(self, request, *args, **kwargs):
        serializer = BulkPurchaseHistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_items = serializer.save()
        return Response(
            PurchaseHistorySerializer(created_items, many=True).data,
            status=status.HTTP_201_CREATED
        )

class PurchaseHistoryDeleteAll(generics.DestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
