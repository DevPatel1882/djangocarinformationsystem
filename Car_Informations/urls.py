"""Car_Informations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('master/',views.master,name='master'),

    #contact url
    path('contact/',views.contact_us,name='contact'),

    # Login url
    path('login/',views.handlelogin,name="login"),
    path('signup/',views.handlesignup,name="signup"),

    # sell car url

    path('sellcar/',views.sell_car,name='sell_car'),
    path('sellcardetails/',views.sell_car_details,name='sell_car_details'),
    path('sellcardetails/<str:id>',views.seller_info,name='sellerinfo'),


    # cars url
    path('maruti/',views.maruti_cars,name='maruti'),



    path('maruti/<str:car_name>',views.maruti_info,name='maruti_info'),

    #  cars url

    path('tata/',views.tata,name='tata'),
    path('jaguar/',views.jaguar,name='jaguar'),
    path('mahindra/',views.mahindra,name='mahindra'),
    path('hundai/',views.hundai,name='hundai'),
    path('honda/',views.honda,name='honda'),
    path('ford/',views.ford,name='ford'),
    path('nissan/',views.nissan,name='nissan'),
    path('renult/',views.renult,name='renult'),


    #  cars informations url
    path('tata/<str:car_name>',views.car_info,name='car_info'),
    path('jaguar/<str:car_name>',views.car_info,name='car_info'),
    path('mahindra/<str:car_name>',views.car_info,name='car_info'),
    path('hundai/<str:car_name>',views.car_info,name='car_info'),
    path('honda/<str:car_name>',views.car_info,name='car_info'),
    path('ford/<str:car_name>',views.car_info,name='car_info'),
    path('renult/<str:car_name>',views.car_info,name='car_info'),
    path('nissan/<str:car_name>',views.car_info,name='car_info'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
