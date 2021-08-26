from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from visitors.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


class BookingListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Booking
    template_name = 'staff/booking_list.html'
    def test_func(self):
        return self.request.user.is_staff


class StaffBookingView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Booking
    template_name = 'staff/booking.html'    
    def test_func(self):
        return self.request.user.is_staff

class BookingDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Booking
    template_name = 'staff/delete_booking.html'
    success_url = reverse_lazy('staff_view_bookings') 
    def test_func(self):
        return self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        messages.warning(request,f'YOU JUST DELETED {self.object}')
        self.object.delete()
        return HttpResponseRedirect(success_url)

class BookingCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Booking
    fields = '__all__'
    template_name = 'staff/add.html'
    success_url = reverse_lazy('staff_view_bookings')   
    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        booking = form.save(commit=False)
        if booking.is_available():
            booking.save()
            return super().form_valid(form)
        else:   
            return super().form_invalid(form) 
          
class BookingUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Booking
    fields = '__all__'
    template_name = 'staff/update.html'
    success_url = reverse_lazy('staff_view_bookings')
    def test_func(self):
        return self.request.user.is_staff


class ReviewDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Review
    template_name = 'staff/delete_review.html'
    success_url = reverse_lazy('review') 
    def test_func(self):
        return self.request.user.is_staff

# class StaffAllContactView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
#     model = Contact
#     template_name = 'staff/all_contact.html'    
#     def test_func(self):
        return self.request.user.is_staff

def allcontacts(request):
    context = {'contacts': Profile.objects.all()}
    return render(request,'staff/all_contacts.html', context )




class StaffCreateContactView(CreateView):
    model = Contact
    fields = ['message']
    success_url = reverse_lazy('staff_all_contacts')
    template_name = 'staff/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = Profile.objects.get(id =self.kwargs['pk'])       
        context['contacts'] = Contact.objects.filter(profile = person)
        print(context)
        return context

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.author = self.request.user.first_name
        person = Profile.objects.get(id =self.kwargs['pk'])       

        contact.profile = person
        contact.save()
        return super().form_valid(form)        
