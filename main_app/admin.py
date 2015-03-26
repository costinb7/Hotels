from django.contrib import admin
from main_app.models import Hotels, Owners, Zones, Cities, Reviews

# Register your models here.
admin.site.register(Hotels)
admin.site.register(Owners)
admin.site.register(Zones)
admin.site.register(Cities)
admin.site.register(Reviews)
