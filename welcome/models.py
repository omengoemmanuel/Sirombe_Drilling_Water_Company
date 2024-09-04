from django.db import models


# Create your models here.

class blog_page(models.Model):
    date = models.DateField()
    blog_name = models.CharField(max_length=50, null=False, blank=False)
    blog_description = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/blogs', default='uploads/blogs/blog.jpg')

    def __str__(self):
        return self.blog_name
    