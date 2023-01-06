from django.urls import path,include
from . import views

urlpatterns = [
    # menu
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    # groups
    path('groups/manager/users/', views.ManagerView.as_view()),
    path('groups/manager/users/<int:pk>/', views.DeleteUserView.as_view()),
    path('groups/delivery-crew/users/', views.DeliveryCrewView.as_view()),
    path('groups/delivery-crew/users/<int:pk>/', views.DeleteDeliveryCrew.as_view()),
    # cart
    path('cart/menu-items/', views.CartView.as_view()),
    # orders
    path('orders/', views.OrdersView.as_view()),
    path('orders/<int:pk>/', views.OrderIdView.as_view()), 
    
    
]