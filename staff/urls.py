from django.urls import path,include
from . import views
# from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('view_bookings/', views.BookingListView.as_view(), name = 'staff_view_bookings'),
    path('booking/<int:pk>', views.StaffBookingView.as_view(), name = 'staff_booking_detail'),
    path('delete_booking/<int:pk>', views.BookingDeleteView.as_view(), name = 'staff_delete_booking'),
    path('add_booking', views.BookingCreateView.as_view(), name = 'staff_create_booking'),
    path('update_booking/<int:pk>',views.BookingUpdateView.as_view(), name ='staff_update_booking'),
    path('delete_review/<int:pk>', views.ReviewDeleteView.as_view(), name = 'staff_delete_review'),
    path ('all_contacts/',views.allcontacts, name='staff_all_contacts'),
    path('all_contact/<pk>',views.StaffCreateContactView.as_view(),name='staff_contact')
    # path('', views.homepage, name='staff'),
    # path('signup/', views.SignupView.as_view(), name='signup' ),

]