from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)  # this will allow us to see the Post model in the admin page
