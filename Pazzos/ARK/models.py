from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PazzosUser(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F','Female'),
        )
    HAND = (
        ('L', 'Left'),
        ('R', 'Right'),
        ('A','Ambi'),
        )
    ENGLISH = (
        ('B','Beginner'),
        ('M', 'Moderate'),
        ('E', 'Expert'),
        ('F', 'Fluent')
        )
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices = GENDER)
    handedness = models.CharField(max_length = 1, choices = HAND)
    english_level = models.CharField(max_length = 1, choices = ENGLISH)
    
User.profile = property(lambda u : PazzosUser.objects.get_or_create(user = u)[0])