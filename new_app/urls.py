from django.urls import path

from new_app import views

urlpatterns = [
    path('login',views.Login,name='login'),
    path('seller',views.seller,name='seller'),
    path('customer',views.customer,name='customer'),
    path("index_dashboard",views.index_dashboard,name='index_dashboard'),
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('view',views.view,name='view')

]