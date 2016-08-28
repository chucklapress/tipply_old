from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from tipplyapi.permissions import IsOwnerOrReadOnly


from tipplyapi.serializers import EmployeeListingSerializer
from app.models import EmployeeListing
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

class EmployeeListingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeListing.objects.all()
    serializer_class = EmployeeListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
