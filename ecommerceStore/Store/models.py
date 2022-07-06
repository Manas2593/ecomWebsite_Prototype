from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            return ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.active = is_active
        user.admin = is_superuser
        user.staff = is_staff
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_staffuser(self, email, password=None):
        user =  self.create_user(
            email = email,
            password = password,
            is_staff = True
        )
        return user


    def create_superuser(self, email, password=None):
        user =  self.create_user(
            email = email,
            password = password,
            is_staff = True,
            is_superuser = True
        )
        return user


    







class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, null=True, unique=True)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'


    objects = UserManager()

    def __str__ (self) -> None:
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True



