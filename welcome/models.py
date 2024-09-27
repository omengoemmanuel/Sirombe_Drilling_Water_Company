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

    def __str__(self):
        return self.fname


class booking(models.Model):
    query_choice = [
        ('Select Your Query Type', 'Select Your Query Type'),
        ('Surveys and Local Fees', 'Surveys and Local Fees'),
        ('Drilling Services', 'Drilling Services'),
        ('Pump Installation', 'Pump Installation')
    ]
    query_type = models.CharField(max_length=50, null=False, blank=False, choices=query_choice)
    location = models.CharField(max_length=50, null=False, blank=False)
    pick_date = models.DateField()
    pick_time = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.query_type
