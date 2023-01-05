from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.http import HttpRequest
from django.contrib.auth.models import User

# --------------------------------------------
# menuitems
# --------------------------------------------
class MenuItemsView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # ordering_fields = ['price','inventory']
    # filterset_fields = ['price','inventory']
    # search_fields = ['category']
    
class SingleMenuItemView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
# -------------------------------------------- 
# manager
# --------------------------------------------
class ManagerView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    

class DeleteUserView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

# --------------------------------------------
# deliverycrew
# --------------------------------------------
class DeliveryCrewView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    

class DeleteDeliveryCrew(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    

# --------------------------------------------
# cart
# --------------------------------------------
class CartView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
     serializer_class = CartSerializer
     queryset = Cart.objects.all()
     permission_classes = [IsAuthenticated,DjangoModelPermissions]
     def get_queryset(self):
         return Cart.objects.all().filter(user=self.request.user)

# --------------------------------------------
# orders
# --------------------------------------------
class OrdersView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            print(self.request.user.groups.name)
            return OrderItem.objects.all()
        elif self.request.user.groups.filter(name = 'Delivery Crew').exists():
            return OrderItem.objects.all().filter(delivery_crew=self.request.user)

        else:
            return OrderItem.obItemjects.all().filter(user=self.request.user)
     

class OrderIdView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return Order.objects.all()
        elif self.request.user.groups.filter(name = 'Delivery Crew').exists():
            return Order.objects.all().filter(delivery_crew=self.request.user)

        else:
            return Order.objects.all().filter(user=self.request.user)
