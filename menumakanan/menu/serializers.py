from rest_framework import serializers
from .models import MenuItem, PurchaseHistory

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'image', 'price']

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ['id', 'title', 'image', 'price']

class BulkPurchaseHistorySerializer(serializers.Serializer):
    items = PurchaseHistorySerializer(many=True)

    def create(self, validated_data):
        items = validated_data.get('items', [])
        purchase_history = [PurchaseHistory(**item) for item in items]
        created = PurchaseHistory.objects.bulk_create(purchase_history)
        return created
