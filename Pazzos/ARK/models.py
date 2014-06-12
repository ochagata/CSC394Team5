import datetime
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, BaseUserManager, AbstractBaseUser
import pdb

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
                          last_name = last_name, is_staff = True,
                          is_admin = True, is_superuser = True)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
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
    age = models.IntegerField(blank = True)
    gender = models.CharField(max_length = 1, choices = GENDER, blank = True)
    handedness = models.CharField(max_length = 1, choices = HAND, blank = True)
    english_level = models.CharField(max_length = 1, choices = ENGLISH, blank = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PazzosUserManager()
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_short_name(self):
        return self.first_name + " " + self.last_name[0] + "."
    
    def __str__(self):
        return "Name: " + self.get_full_name() + ". Email: " + self.email

#word model: the "dictionary" where we should grab our words from for each test
class PazzosTestWord(models.Model):
    word = models.CharField(unique = True, db_index = True, max_length = 255)
    wordLength = models.IntegerField()

    def __str__(self):
        return self.word
    
class PazzosTest(models.Model):
    takenBy = models.ForeignKey(PazzosUser)
    timeStarted = models.TimeField( default = datetime.datetime.now().time() )
    timeCompleted = models.TimeField( default = datetime.datetime.now().time() )

    #when django binds manytomanyfields to the sqlite database, it tries to create a corresponding link in the model that
    #we specify which uses the name of the model in question. adding a related name allows more than one attribute to have
    #references to the same model. these related_names must be unique
    word_list = models.ManyToManyField(PazzosTestWord, related_name = "pazzostest_word_set")
    correct_list = models.ManyToManyField(PazzosTestWord, related_name = "pazzostest_correct_set")

    def __str__(self):
        return str(self.id)
