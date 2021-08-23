from django.db import models

# Create your models here.
class Post(models.Model):
    class Passenger(models.Model):
        # Attribute Variables for Driver class to represent different columns in database
        '''
        name-: This is the name of the passenger
        avatar-: A picture of the rider
        pickup_location-: Connected to the Location class using a FOREIGN_KEYz
        '''
        name = models.OneToOneField(User, related_name='rider_profile', on_delete=models.CASCADE)
        bio = models.CharField(max_length=60)
        avatar = models.ImageField(upload_to='ProfilePicture/')
        current_location = models.ForeignKey('uber.Location', related_name='current_location', on_delete=models.CASCADE,
                                             null=True)
        pickup_location = models.ForeignKey('uber.Location', related_name='rider_pickup', on_delete=models.CASCADE)
        contact_info = models.CharField(max_length=50)

        '''Method to filter database results'''

        def __str__(self):
            return self.name
