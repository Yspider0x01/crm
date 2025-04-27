from django.urls import path 
from . import views

urlpatterns = [
    path("" ,views.index , name="index"),
    path("register/" , views.register , name="register"),
    path('login/' , views.sign_in  , name='login'),
    path('dashboard/' , views.dashboard , name="dashboard"),
    path("logout/" , views.logoutView , name='logout'),
    path("create-record/"  , views.create_record , name='create_record'),
    path('view/<int:id>/' , views.view_record , name="view_record" ),
    path("update/<int:id>/" , views.update_record , name="update_record"),
    path("delete/<int:id>/" , views.delete_record , name="delete_record"),
    path("search/" , views.search , name="search")
]
