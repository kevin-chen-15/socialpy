from django.db import models
from django.conf import settings
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/username/<filename>
    return '{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to=user_directory_path, default='default/default.jpg')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {}'.format(self.name)
