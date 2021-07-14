from django.db import models
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    default_type = 'type1'
    types= (
        ('type1', 'type1'),
        ('type2', 'type2'),
        ('type3', 'type3'),
        
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True,upload_to='images/')
    account_type= models.CharField(max_length=50,choices=types,default=default_type,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.account_type} - {self.user.username}'

    class Meta:
        verbose_name_plural = 'Profile'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'],
        )
post_save.connect(create_profile, sender=User)