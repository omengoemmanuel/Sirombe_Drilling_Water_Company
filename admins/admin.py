from django.contrib import admin
from .models import survey, userprofile, survey_and_local_fee, Survey_Application, profile_photo

# Register your models here.
admin.site.register(survey)
admin.site.register(userprofile)
admin.site.register(survey_and_local_fee)
admin.site.register(Survey_Application)
admin.site.register(profile_photo)
