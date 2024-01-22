from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    birthday = models.DateField()
    status = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="photos/%Y/")

class Dogs(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/")

class Record(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    cynologyst = models.ForeignKey('User', on_delete=models.PROTECT, related_name='user')
    dogs = models.ForeignKey('Dogs', on_delete=models.PROTECT)
    date = models.DateField()
    time = models.TimeField()
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)

class Price(models.Model):
    people_cynologist = models.IntegerField()
    group_cynologist = models.IntegerField()
    people_single = models.IntegerField()
    group_single = models.IntegerField()
    date_price = models.DateField(auto_now_add=True)