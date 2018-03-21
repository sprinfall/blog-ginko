# -*- coding: utf-8 -*-

# import os

from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.template.defaultfilters import slugify


#-------------------------------------------------------------------------------

# TODO
# 1. Case insensitive
#    "c++" == "C++", "travel" == "TRAVEL", etc.
#    Convert a given tag name to lower case then use it as primary key.
# 2. Alias
#    E.g., "徕卡" == "Leica"

class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return 'Tag: {}'.format(self.name)


#-------------------------------------------------------------------------------

class Post(models.Model):

    title = models.CharField(max_length=256)

    content = models.TextField()

    create_time = models.DateTimeField('Date time published',
                                       auto_now_add=True)

    last_update_time = models.DateTimeField('Date time last updated.',
                                            auto_now_add=True)

    # A post has multiple tags while tag belongs to multiple posts.
    # So it's a Many-To-Many relationship.
    tags = models.ManyToManyField(Tag)


#-------------------------------------------------------------------------------

class Picture(models.Model):

    # def image_upload_to(self, filename):
    #     """
    #     Compute the upload path for the image field.
    #     """
    #     now = timezone.now()
    #     filename, extension = os.path.splitext(filename)
    #
    #     return os.path.join(
    #         UPLOAD_TO,
    #         now.strftime('%Y'),
    #         now.strftime('%m'),
    #         now.strftime('%d'),
    #         '%s%s' % (slugify(filename), extension))

    # A post has multiple pictures.
    post = models.ForeignKey(Post, related_name='pictures',
                             on_delete=models.CASCADE)

    # TODO: upload_to='%Y/%m/%d'
    image = models.ImageField(upload_to="uploads")

    # For ordering: 1, 2, 3, etc.
    order = models.SmallIntegerField(default=0)
