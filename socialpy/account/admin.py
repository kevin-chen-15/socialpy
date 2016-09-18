from django.contrib import admin
from .models import Profile, Comment

#List Profiles by username, date of birth, and photo file
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

#Display Profiles under the Account section of the Django Admin page. 
admin.site.register(Profile, ProfileAdmin)

#List Comments by name, the user profile the comment is posted on, when it is created, and if it is active. 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')

#Display Comments under the Account section of the Django Admin page. 
admin.site.register(Comment, CommentAdmin)

def __unicode__(self):
    return self.text

