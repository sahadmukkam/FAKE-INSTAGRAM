from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.reg,name='login'), 
    path('sign/', views.sign,name='sign'),
    path('logout/', views.logout_view,name='logout'),
    path('activate/<uidb64>/<token>/',views.activate)

]