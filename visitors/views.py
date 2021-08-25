from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm, EditUserForm, EditProfileForm,BookingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def rooms(request):
    return render(request, 'rooms.html', {'rooms': Room.objects.all() })

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

class UpdateProfile(LoginRequiredMixin,UpdateView):
    form_class = EditProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = EditUserForm(instance=self.request.user)
        return context
    
    def get_object(self, queryset= None):
        return self.request.user.profile

    def form_valid(self, form):
        user_form = EditUserForm(self.request.POST, instance = self.reuest.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

class RoomTypeView(CreateView):
    model = RoomType
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy('home')

class RoomView(CreateView):
    model = Room
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy('home')    

class BookingView(DetailView):
    model = Booking
    template_name = 'booking.html'

class CreateBookingView(CreateView):
    form_class = BookingForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    
    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.profile = self.request.user.profile
        booking.room_id = self.kwargs['pk']
        if booking.is_available():
            booking.save()
            return super().form_valid(form)
        else:   
            return super().form_invalid(form) 
        # for book in Booking.objects.filter(room =booking.room):
        #     if booking.book_start >= book.book_start and booking.book_end <= book.book_end:
        #         return super().form_invalid(form)                    
        #     elif booking.book_start <= book.book_start and booking.book_end >= book.book_end:
        #         return super().form_invalid(form)
        # booking.save()
        # print('booking worked')
        # return super().form_valid(form)
