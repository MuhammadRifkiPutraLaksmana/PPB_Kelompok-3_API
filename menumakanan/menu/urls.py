from django.urls import path
from .views import MenuItemList
from .views import PurchaseHistoryListCreate, PurchaseHistoryDeleteAll

urlpatterns = [
    path('menu-items/', MenuItemList.as_view(), name='menu-item-list'),
    path('purchase-history/', PurchaseHistoryListCreate.as_view(), name='purchase-history'),
     path('purchase-history/delete-all/', PurchaseHistoryDeleteAll.as_view(), name='purchase-history-delete-all'),
]
