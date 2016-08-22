from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from app.models import EmployeeListing
from tipplyapi.serializers import EmployeeListingSerializer
# Create your views here.

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user

class EmployeeListingListAPIView(generics.ListCreateAPIView):
    queryset = EmployeeListing.objects.all()
    serializer_class = EmployeeListingSerializer
