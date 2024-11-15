from django.db import models



class blogmodel(models.Model):
    title = models.CharField(max_length=50, default="enter title")
    content = models.TextField(max_length=300, verbose_name="content")
    publication_date = models.DateField()
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog_images',default="default.png", blank=True, null=True)

    def __str__(self):
        return self.title



# Create your models here.
