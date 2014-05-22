from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

class PazzosUser(models.model):
    user = models.OneToOneField(User),
    gender = (('M', 'Male'),('F','Female')),
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)]),
    handedness = (('L', 'Left'), ('R', 'Right'), ('A','Ambi'))
    english_level = (('B','Beginner'), ('M', 'Moderate'), ('E', 'Expert'), ('F', 'Fluent'))