from django.db import models
from django.core.files.storage import FileSystemStorage



# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.title + 'by' + self.author

    class Meta:
        db_table = "post"