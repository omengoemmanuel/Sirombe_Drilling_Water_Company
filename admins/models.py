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
    profile_photos = models.FileField(upload_to='uploads/profile', default='uploads/profile/profile.jpg', null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class survey_and_local_fee(models.Model):
    industrial_survey_fee = models.PositiveIntegerField()
    industrial_local_authority_fee = models.PositiveIntegerField()
    commercial_survey_fee = models.PositiveIntegerField()
    commercial_local_authority_fee = models.PositiveIntegerField()
    domestic_survey_fee = models.PositiveIntegerField()
    domestic_local_authority_fee = models.PositiveIntegerField()


class Survey_Application(models.Model):
    Survey_Category = models.CharField(max_length=50, null=False, blank=False)
    First_Name = models.CharField(max_length=20, null=False, blank=False)
    Last_Name = models.CharField(max_length=20, null=False, blank=False)
    Email_Address = models.EmailField(null=False, blank=False)
    Phone_Number = models.PositiveIntegerField(null=False, blank=False)
    Survey_Fee = models.PositiveIntegerField(null=False, blank=False)
    Local_Authority_Fee = models.PositiveIntegerField(null=False, blank=False)
    Total_Amount = models.PositiveIntegerField(null=False, blank=False)
    Mpesa_phone = models.PositiveIntegerField(blank=False, null=True, default='0000000000')
    Amount_paid = models.PositiveIntegerField(blank=False, null=True, default='0')

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"


