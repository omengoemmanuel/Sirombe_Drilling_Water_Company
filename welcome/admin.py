from django.contrib import admin
from .models import blog_page, messagess, booking

# Register your models here.
admin.site.register(blog_page)
admin.site.register(messagess)
admin.site.register(booking)
