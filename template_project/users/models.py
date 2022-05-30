from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_constraint=False)
    image = models.ImageField(default='profile_avatars/default.jpg', upload_to='profile_avatars')

    title = models.CharField(max_length=64, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)



# from django.contrib.auth.models import User
# from django.db import models
# from django.contrib import auth
# from django.utils import timezone

# # Create your models here.

# class User(auth.models.User, auth.models.PermissionsMixin):
#     def __str__(self):
#         return f"@{self.username}"

