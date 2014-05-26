from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, BaseUserManager, AbstractBaseUser

class PazzosUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password = None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Your first name is required')
        if not last_name:
            raise ValueError('Your last name is required')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def create_superuser(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Your first name is required')
        if not last_name:
            raise ValueError('Your last name is required')
        if not password:
            raise ValueError('Password is required')
        user = self.model( email = self.normalize_email(email),
                          first_name = first_name,
                          last_name = last_name)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    

# Create your models here.
class PazzosUser(AbstractBaseUser, PermissionsMixin):
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
    email = models.EmailField(max_length = 255, unique = True, db_index = True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices = GENDER)
    handedness = models.CharField(max_length = 1, choices = HAND)
    english_level = models.CharField(max_length = 1, choices = ENGLISH)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    
    objects = PazzosUserManager()
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_short_name(self):
        return self.first_name + " " + self.last_name[0] + "."
    
    def __str__(self):
        return "Name: " + self.get_full_name() + ". Email: " + self.email
    
    
    
    
    
#    
#User.profile = property(lambda u : PazzosUser.objects.get_or_create(user = u)[0])