from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

from ckeditor.fields import RichTextField
from PIL import Image

from blog.helpers import unique_post_slug_generator


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=124)
    content = RichTextField()
    cover_image = models.ImageField(
        default='blog-cover-photos/default.png', upload_to='blog-cover-photos/%Y/%m/%d/')
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]

    def save(self):
        self.slug = unique_post_slug_generator(self)
        super(Post, self).save()


class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='author-avatars/default.jpeg', upload_to='author-avatars/%Y')
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True,
                              help_text='Enter URL to anywhere on the web we can find your content.')
    twitter = models.URLField(blank=True, null=True,
                              help_text='Enter URL to your twitter profile.')
    facebook = models.URLField(
        blank=True, null=True, help_text='Enter URL to your facebook profile.')
    instagram = models.URLField(
        blank=True, null=True, help_text='Enter URL to your instagram profile.')

    def __str__(self):
        return self.user.get_full_name()

    def save(self):
        super(AuthorProfile, self).save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
