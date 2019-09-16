from django.urls import path , include

from . import views

app_name = 'curd_app'

urlpatterns = [

    path('', views.home ,name='home' ),

    path('submit/', views.submit , name ='submit'),

    path('edit/<int:base_id>', views.edit , name = 'edit'),

    path('update/<int:base_id>', views.update , name = 'update'),

    path('delete/<int:base_id>', views.delete_rec , name = 'delete'),
    
]