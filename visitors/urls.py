from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.homepage, name='home'),
    path('signup/', views.SignupView.as_view(), name='signup' ),
    path('profile/', views.UpdateProfile.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_room_type', views.RoomTypeView.as_view(), name = 'create_room_type'),
    path('add_room', views.RoomView.as_view(), name = 'create_room'),
    path('rooms/', views.rooms,name= 'rooms'),
    path('booking/<int:pk>', views.BookingView.as_view(), name = 'booking_detail'),
    path('create_booking/<int:pk>', views.CreateBookingView.as_view(), name = 'create_booking'),


]
