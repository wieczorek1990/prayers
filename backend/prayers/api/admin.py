from django.contrib import admin

from api import models

routes = (
    (models.PrayerRequest, None,),
    (models.Prayer, None,),
    (models.PrayerEvent, None,),
)

for model, admin_model in routes:
    admin.site.register(model, admin_class=admin_model)
