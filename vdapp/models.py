from django.db import models

# Create your models here.


class Index(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    video = models.FileField(upload_to='video/%y')

    def __str__(self):
        return self.title
