from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

# --------------------------------------------
# menuitems
# --------------------------------------------
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [DjangoModelPermissions]
    ordering_fields = ['price','featured']
    filterset_fields = ['price','featured']
    search_fields = ['category']
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [DjangoModelPermissions]
    
# -------------------------------------------- 
# manager
# --------------------------------------------
class ManagerView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return User.objects.all()
        else:
            raise PermissionDenied() 

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return User.objects.all()
        else:
            raise PermissionDenied() 

# --------------------------------------------
# deliverycrew
# --------------------------------------------
class DeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return User.objects.all()
        else:
            raise PermissionDenied()
class DeleteDeliveryCrew(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return User.objects.all()
        else:
            raise PermissionDenied()    
# --------------------------------------------
# cart
# --------------------------------------------
class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
     serializer_class = CartSerializer
     queryset = Cart.objects.all()
     permission_classes = [IsAuthenticated,]
     def get_queryset(self):
            return Cart.objects.all().filter(user=self.request.user)

# --------------------------------------------
# orders
# --------------------------------------------
# create order
class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]
    ordering_fields = ['order','price']
    filterset_fields = ['order','price']
    search_fields = ['menuitem']

    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return OrderItem.objects.all()
        elif self.request.user.groups.filter(name = 'Delivery Crew').exists():
            return OrderItem.objects.all().filter(delivery_crew=self.request.user)

        else:
            return OrderItem.objects.all().filter(order=self.request.user)
     
# to manage already orders
class OrderIdView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = OrderDetail.objects.all()
    permission_classes = [IsAuthenticated,]
    ordering_fields = ['user','delivery_crew','status','total','date']
    filterset_fields = ['user','delivery_crew','status','total','date']
    search_fields = ['user','delivery_crew','status','total','date']
    def get_queryset(self):
        if self.request.user.groups.filter(name = 'Manager').exists():
            return OrderDetail.objects.all()
        elif self.request.user.groups.filter(name = 'Delivery Crew').exists():
            return OrderDetail.objects.all().filter(delivery_crew=self.request.user)

        else:
            return OrderDetail.objects.all().filter(user=self.request.user)