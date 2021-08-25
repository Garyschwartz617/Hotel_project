from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class RoomType(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    beds = models.IntegerField()

    def __str__(self):
        return f'{self.beds} bedroom {self.name}'

class Room(models.Model):
    room_type = models.ForeignKey(RoomType,on_delete=CASCADE)

    # def is_available(self):
    #     for booking in self.booking_set.all():
    #         if booking.book_start and booking.book_end:
    #             return False 
    #     return True



#  for book in Booking.objects.filter(room =booking.room):
#             if booking.book_start >= book.book_start and booking.book_end <= book.book_end:
#                 return super().form_invalid(form)                    
#             elif booking.book_start <= book.book_start and booking.book_end >= book.book_end:
#                 return super().form_invalid(form)



class Booking(models.Model):    
    room = models.ForeignKey(Room, on_delete=CASCADE)
    people = models.IntegerField()
    book_start = models.DateTimeField(auto_now_add=False)
    book_end = models.DateTimeField(auto_now_add=False)
    profile = models.ForeignKey(Profile,on_delete=CASCADE)

    def is_available(self):
        for booking in self.room.booking_set.all():
            if self.book_start >= booking.book_start and self.book_start <= booking.book_end:
                return False 
            elif self.book_start <= booking.book_start and self.book_end >= booking.book_end:
                return False
        return True