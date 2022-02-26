from django.contrib import admin
from django.urls import path,include
from sigma import views
admin.site.site_header="Sigma Superuser"
admin.site.site_title="Sigma"
admin.site.index_title="Welcome to Sigma Admin Portal"
urlpatterns = [
    path('signin',views.sign,name='Sign In/Sign Up') 
]