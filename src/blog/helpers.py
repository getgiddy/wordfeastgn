import string
from django.utils.text import slugify
import random


def random_string_generator(size=16, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_post_slug_generator(post, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(post.title)
    instance_class = post.__class__
    qs_exists = instance_class.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_post_slug_generator(post, new_slug=new_slug)
    return slug
