from datetime import datetime

from django.db import models



# Create your models here.



class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def __str__(self):
        return 'Message From ' + self.name+ ' - ' + self.email + ' - ' + self.phone


class BagicTagMaster(models.Model):
    id = models.AutoField(primary_key=True)
    sub_category = models.CharField(max_length=500)
    is_deleted = models.BooleanField(max_length=50, default=False)
    created_by = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50, null=True)


class BagicApiData(models.Model):
    id = models.AutoField(primary_key=True)
    cat_id = models.CharField(max_length=10, null=False)
    category = models.CharField(max_length=20, null=False)
    news_datePublished = models.CharField(max_length=20, null=False)
    news_id = models.CharField(max_length=10, null=False)
    news_title = models.CharField(max_length=100, null=False)
    news_summary = models.TextField()
    news_url = models.CharField(max_length=100, null=False)
    news_coverImage = models.CharField(max_length=100, null=False, default='')
    news_contact = models.CharField(max_length=12, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    identifier = models.CharField(max_length=30, default='', null=False)
    lang_code = models.CharField(max_length=2, default='', null=False)
    sub_category = models.IntegerField()


