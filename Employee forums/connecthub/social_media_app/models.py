from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

class Posts(models.Model):
    post_pic = models.ImageField(upload_to='post_images/',blank = True,null=True)
    post_bio = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="user_posts")
    date_created = models.DateTimeField(auto_now_add=True)
    
    

