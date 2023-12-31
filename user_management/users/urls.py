from django.urls import path
from .views import create_user, user_list, update_user, delete_user

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('list/', user_list, name='user_list'),
    path('update/<int:user_id>/', update_user, name='update_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
