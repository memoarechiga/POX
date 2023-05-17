from django.urls import path
from .views import Dashboard, MenuItemList, NewItem, OrderView, TorItemUpdate, TorItemDelete

urlpatterns = [
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('menu_item_list', MenuItemList.as_view(), name='menu_item_list'),
    path('new_item', NewItem.as_view(), name='new_item'),
    path('new_sale', OrderView.as_view(), name='new_sale'),
    path('update_item/<int:pk>/', TorItemUpdate.as_view(), name="update_item"),
    path('delete_item/<int:pk>/', TorItemDelete.as_view(), name="delete_item"),
]   
