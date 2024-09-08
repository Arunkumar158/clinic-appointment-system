"""
URL configuration for pro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from.import views


urlpatterns = [
    path('add_doctor',views.add_doctor), 
    path('doctorview',views.doctor_list),
    path('doc_delete/<int:id>',views.doc_delete,name="doc_delete"),
    path('doc_update/<int:id>',views.doc_update,name="doc_update"),
    path('doc_update/doc_updates/<int:id>',views.doc_updates,name="doc_updates"),
    path('regdata',views.regdata),
    path('update_user_profile/<int:id>',views.update_user_profile,name="update_user_profile"),
    path('update_user_profiles/update_user_profiles/<int:id>',views.update_user_profiles,name="update_user_profiles"),

   

]  