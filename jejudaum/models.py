from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Room_info(models.Model):
    owner = models.ForeignKey(User, null=True)
    rome_num = models.AutoField(primary_key=True) #방 번호 인덱스
    owner_pho_num = models.CharField(max_length=50) # 주인 폰번
    deposit = models.IntegerField() # 보증금
    monthly = models.IntegerField() # 월세
    manage_money = models.IntegerField() # 관리비
    rome_name = models.CharField(max_length=50) # 방 이름
    rome_area = models.IntegerField() # 방 면적
    total_floor = models.IntegerField() # 총 층수
    rome_floor = models.IntegerField() # 그방의 층수
    detail_address = models.CharField(max_length=50) # 상세 주소
    create_date = models.DateTimeField( #날째
            blank=True, null=True, auto_now_add = True);

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.rome_name

class Option_info(models.Model):
    rome_num = models.ForeignKey(Room_info, on_delete=models.CASCADE) #방의 모델 관계키
    parking = models.BooleanField(default=False) # 주차가능?
    elevator = models.BooleanField(default=False) # 엘베 있어?
    animal = models.BooleanField(default=False) # 애완동물 가능?
    aricon = models.BooleanField(default=False) # 에어컨 가능?
    washer = models.BooleanField(default=False) # 개인 세탁기 가능?
    freezer = models.BooleanField(default=False) # 냉장고 가능?
    tv = models.BooleanField(default=False) # 티비 있어?
    doorlock = models.BooleanField(default=False) # 도어락 있어?
    bed = models.BooleanField(default=False) #침대 있어?

class Address(models.Model):
    rome_num = models.ForeignKey(Room_info, on_delete=models.CASCADE) # 방 연결 키
    city = models.CharField(max_length=50) # 제주시 인지 서귀포 시 이진지
    town = models.CharField(max_length=50) # 애월읍 노형동 그런거
    village = models.CharField(max_length=50) # 마을이름 대표적으로 봉성리
