from django.db import models


# Create your models here.

class blog_page(models.Model):
    date = models.DateField()
    blog_name = models.CharField(max_length=50, null=False, blank=False)
    blog_description = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/blogs', default='uploads/blogs/blog.jpg')

    def __str__(self):
        return self.blog_name


class messagess(models.Model):
    fname = models.CharField(max_length=20, null=False, blank=False)
    lname = models.CharField(max_length=20, null=False, blank=False)
    phone = models.IntegerField()
    mail = models.EmailField()
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname


class booking(models.Model):
    query_type = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    pick_date = models.DateField()
    pick_time = models.TimeField()
    name = models.CharField(max_length=255, null=False, blank=False, default="XXXXXXXX")
    phone = models.CharField(max_length=13, null=False, blank=False, default="XXXXXXXX")

    def __str__(self):
        return self.name
