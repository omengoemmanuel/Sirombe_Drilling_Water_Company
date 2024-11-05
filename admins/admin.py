from django.contrib import admin
from .models import survey, userprofile, survey_and_local_fee, Survey_Application, Payment, Pump, Tank, drilling_and_pump_installation

# Register your models here.
admin.site.register(survey)
admin.site.register(userprofile)
admin.site.register(survey_and_local_fee)
admin.site.register(Survey_Application)
admin.site.register(Payment)
admin.site.register(Pump)
admin.site.register(Tank)
admin.site.register(drilling_and_pump_installation)


