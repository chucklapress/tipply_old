"""tipply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from rest_framework.authtoken import views
from app.views import IndexView,SignUpView,LoginView,LogoutView,EmployeeListingCreateView,ApplicantListView
from tipplyapi.views import EmployeeListingListAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^signup/$', SignUpView.as_view(), name='sign_up_view'),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^employee_listing_create/$',EmployeeListingCreateView.as_view(), name='employee_listing_create_view'),
    url(r'^applicant_list/$',ApplicantListView.as_view(), name='applicant_list_view'),
    url(r'^api/employee_listings/$', EmployeeListingListAPIView.as_view(), name="employee_listing_list_api_view")

]
