from django.db import models

from django.contrib.auth.models import User
# Create your models here.


def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    # masinogns/asdfqwer.png
    return '%s/%s.%s' % (instance.owner.username, pid, extension)

class Photo(models.Model):
    image = models.ImageField(upload_to = user_path)
    owner = models.ForeignKey(User, null=True)
    thumnail_image = models.ImageField(blank = True)
    room_phone = models.CharField(max_length = 255)
    room_name = models.CharField(max_length = 255)
    room_monthly = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)
    upload_date = models.DateTimeField('Upload Date',null=True, auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']
