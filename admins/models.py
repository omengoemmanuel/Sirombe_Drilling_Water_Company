from django.db import models


# Create your models here.
class survey(models.Model):
    client_choices = [
        ('Industrial', 'Industrial'),
        ('Commercial', 'Commercial'),
        ('Domestic', 'Domestic')
    ]
    client_category = models.CharField(max_length=20, null=False, blank=False, choices=client_choices)
    survey_fees = models.PositiveIntegerField(null=False, blank=False)
    local_authority_fees = models.PositiveIntegerField(null=False, blank=False)
    survey_photo = models.ImageField(upload_to="uploads/survey", default="uploads/survey/photo.jpg")

    def __str__(self):
        return self.client_category
