from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from users.managers import UserManager, ActiveUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = models.CharField('username', max_length=50, unique=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[username_validator])
    email = models.EmailField('email address', max_length=255, unique=True)
    name = models.CharField('name', max_length=100)
    avatar_url = models.URLField('avatar', blank=True, null=True)

    is_active = models.BooleanField('active', default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    active = ActiveUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
