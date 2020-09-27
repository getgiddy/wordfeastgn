from django.contrib import admin
from blog.models import AuthorProfile, Post


admin.site.register(Post)
admin.site.register(AuthorProfile)
