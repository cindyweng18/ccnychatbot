from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    # path ('<str:room_name>/', views.room, name = 'room')
    path ('room-list/', views.RoomList.as_view()),
    path ('room-detail/<str:pk>/', views.RoomDetail.as_view()),
    path ('message-list/', views.messageList, name = 'message_list'),
    path ('message-post/<str:room_id>/', views.messagePost, name = 'message_post'),
    path ('message-detail/<str:room_id>/', views.messageDetail, name = 'message_detail'),
]