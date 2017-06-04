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
    owner = models.ForeignKey(User, null=True)
    image = models.ImageField(upload_to = user_path)
    thumnail_image = models.ImageField(blank = True)
    room_phone = models.CharField(max_length = 255)
    room_name = models.CharField(max_length = 255)
    deposit = models.IntegerField(blank = True) # 보증금
    monthly = models.IntegerField(blank = True) # 월세
    manage_money = models.IntegerField(blank = True) # 관리비
    rome_area = models.IntegerField(blank = True) # 방 면적
    detail_address = models.CharField(max_length = 255)
    upload_date = models.DateTimeField('Upload Date',null=True, auto_now_add=True)

    parking = models.BooleanField(default=False) # 주차가능?
    elevator = models.BooleanField(default=False) # 엘베 있어?
    animal = models.BooleanField(default=False) # 애완동물 가능?
    aricon = models.BooleanField(default=False) # 에어컨 가능?
    washer = models.BooleanField(default=False) # 개인 세탁기 가능?
    freezer = models.BooleanField(default=False) # 냉장고 가능?
    tv = models.BooleanField(default=False) # 티비 있어?
    doorlock = models.BooleanField(default=False) # 도어락 있어?
    bed = models.BooleanField(default=False) #침대 있어?

    city = models.CharField(max_length=50) # 제주시 인지 서귀포 시 이진지
    town = models.CharField(max_length=50) # 애월읍 노형동 그런거
    village = models.CharField(max_length=50) # 마을이름 대표적으로 봉성리

    class Meta:
        ordering = ['-upload_date']

# class Option_info(models.Model):
#     rome_num = models.ForeignKey(Photo, on_delete=models.CASCADE) #방의 모델 관계키
#     parking = models.BooleanField(default=False) # 주차가능?
#     elevator = models.BooleanField(default=False) # 엘베 있어?
#     animal = models.BooleanField(default=False) # 애완동물 가능?
#     aricon = models.BooleanField(default=False) # 에어컨 가능?
#     washer = models.BooleanField(default=False) # 개인 세탁기 가능?
#     freezer = models.BooleanField(default=False) # 냉장고 가능?
#     tv = models.BooleanField(default=False) # 티비 있어?
#     doorlock = models.BooleanField(default=False) # 도어락 있어?
#     bed = models.BooleanField(default=False) #침대 있어?
#
# class Address(models.Model):
#     rome_num = models.ForeignKey(Photo, on_delete=models.CASCADE) # 방 연결 키
#     city = models.CharField(max_length=50) # 제주시 인지 서귀포 시 이진지
#     town = models.CharField(max_length=50) # 애월읍 노형동 그런거
#     village = models.CharField(max_length=50) # 마을이름 대표적으로 봉성리
