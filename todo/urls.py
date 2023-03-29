from django.urls import path
from .views import *

urlpatterns = [
    path('', ListToDosView.as_view(), name='index'),
    path('list/<int:list_id>/', ListItemsView.as_view(), name='list'),
    path('list/add/', CreateToDosView.as_view(), name='list-add'),
    path('list/<int:list_id>/item/add/', CreateItemView.as_view(), name='item-add'),
    path('list/<int:list_id>/item/<int:pk>', UpdateItemsView.as_view(), name='item-update'),
    path('list/<int:pk>/delete/', DeleteToDosView.as_view(), name='list-delete'),
    path('list/<int:list_id>/item/<int:pk>/delete/', DeleteItemsView.as_view(), name='item-delete')
]
