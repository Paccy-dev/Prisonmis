from django.contrib import admin
from .models import *

admin.site.register(Crime)
admin.site.register(Prisoner)
admin.site.register(Visitor)
admin.site.register(Leave)
admin.site.register(Release)
admin.site.register(Cell)
admin.site.register(Complaint)

