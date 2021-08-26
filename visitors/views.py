from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm, EditUserForm, EditProfileForm,BookingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *
from django.db.models import Q
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def rooms(request):
    return render(request, 'rooms.html', {'rooms': Room.objects.all() })

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    
    def form_valid(self, form):
        person = form.save(commit=False)
        person.save()
        
        if person.username.endswith('lol'):
            person.is_staff = True
        
        return super().form_valid(form)    
            

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
        user_form = EditUserForm(self.request.POST, instance = self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

class CreateRoomTypeView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = RoomType
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy('home')
    def test_func(self):
        return self.request.user.is_superuser

class CreateRoomView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Room
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy('home')    
    def test_func(self):
        return self.request.user.is_superuser

class BookingView(LoginRequiredMixin,DetailView):
    model = Booking
    template_name = 'booking.html'

class CreateBookingView(LoginRequiredMixin,CreateView):
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

class CreateReviewView(LoginRequiredMixin,CreateView):
    model = Review
    fields =['review']
    success_url = reverse_lazy('review')
    template_name = 'review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        print(context)
        return context

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.profile = self.request.user.profile
        
        contact.save()
        return super().form_valid(form)

class CreateContactView(CreateView):
    model = Contact
    fields = ['message']
    success_url = reverse_lazy('messages')
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.filter(profile = self.request.user.profile)
        print(context)
        return context

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.profile = self.request.user.profile
        contact.author = self.request.user.first_name

        contact.save()
        return super().form_valid(form)
        







        
# class CreateContactView(CreateView):
#     model = Contact
#     fields = ['message']
#     success_url = reverse_lazy('home')
#     template_name = 'contact.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['contacts'] = Contact.objects.all()
#         # context['contacts'] = Contact.objects.filter(user_member= self.request.user.profile)
#         print(context)
#         return context

#     def form_valid(self, form):
#         contact = form.save(commit=False)
#         contact.profile = self.request.user.profile
#         print('hello')
#         print(contact.profile)
#         # BELOW IS A MANY TO MANY FIELD
#         # contact.staff_members = User.objects.filter(is_staff=True)
#         u = User.objects.filter(is_staff=True)
#         contact.staff_members.set(u)
#         print('goodbye')
#         # print(contact.staff_member)
#         print(contact.staff_members)
#         contact.save()
#         return super().form_valid(form)
        
