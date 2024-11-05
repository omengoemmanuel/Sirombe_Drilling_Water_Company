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
    p_photo = models.ImageField(upload_to="uploads/profile", default="uploads/profile/profile.jpg")

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
    depth = models.PositiveIntegerField(blank=False, null=False, default='0')
    height = models.PositiveIntegerField(blank=False, null=False, default='0')
    status_choice = [
        ('Approved', 'Approved'),
        ('Verified', 'Verified')
    ]
    status = models.CharField(max_length=15, null=True, blank=True, default="Verified", choices=status_choice)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"


class Payment(models.Model):
    name_choices = [
        ('Symmetric Drilling', 'Symmetric Drilling'),
        ('Core Drilling', 'Core Drilling',),
        ('Geo-Technical Drilling', 'Geo-Technical Drilling')
    ]
    name = models.CharField(max_length=50, choices=name_choices)
    downpayment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Pump(models.Model):
    pump_choices = [
        ('Submersible Electric Pump', 'Submersible Electric Pump'),
        ('Solar Pump', 'Solar Pump'),
        ('Hand Pump', 'Hand Pump')
    ]
    pump = models.CharField(max_length=100, choices=pump_choices)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.pump


class Tank(models.Model):
    tank_choices = [
        ('Household Tank Plastic', 'Household Tank Plastic'),
        ('Household Steel Tank', 'Household Steel Tank'),
        ('Large Steel Tank', 'Large Steel Tank')
    ]
    tank = models.CharField(max_length=100, choices=tank_choices)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tank


class drilling_and_pump_installation(models.Model):
    serviceType = models.CharField(max_length=50, null=False, blank=False)
    fname = models.CharField(max_length=20, null=False, blank=False)
    lname = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=14, null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False)
    depth = models.PositiveIntegerField()
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    drilling_fee = models.DecimalField(max_digits=10, decimal_places=2)
    pumpType = models.CharField(max_length=50, null=False, blank=False)
    pump_payment = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.PositiveIntegerField()
    pipe_fee = models.DecimalField(max_digits=10, decimal_places=2)
    tankType = models.CharField(max_length=50, null=False, blank=False)
    tank_fee = models.DecimalField(max_digits=10, decimal_places=2)
    pump_tank_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status1_choices = [
        ('In progress', 'In progress'),
        ('On site', 'On site'),
        ('Completed', 'Completed')
    ]
    status1 = models.CharField(max_length=100, default='In progress', choices=status1_choices)

    def __str__(self):
        return f"{self.fname} {self.lname}"



