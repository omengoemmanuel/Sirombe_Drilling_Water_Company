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


class userprofile(models.Model):
    fname = models.CharField(max_length=20, null=False, blank=False)
    lname = models.CharField(max_length=20, null=False, blank=False)
    company = models.CharField(max_length=100, null=False, blank=False)
    job = models.CharField(max_length=100, null=False, blank=False)
    county = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.fname


class survey_and_local_fee(models.Model):
    industrial_survey_fee = models.PositiveIntegerField()
    industrial_local_authority_fee = models.PositiveIntegerField()
    commercial_survey_fee = models.PositiveIntegerField()
    commercial_local_authority_fee = models.PositiveIntegerField()
    domestic_survey_fee = models.PositiveIntegerField()
    domestic_local_authority_fee = models.PositiveIntegerField()
