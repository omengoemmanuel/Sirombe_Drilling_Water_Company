from django.contrib import admin
from .models import survey, userprofile, survey_and_local_fee

# Register your models here.
admin.site.register(survey)
admin.site.register(userprofile)
admin.site.register(survey_and_local_fee)
