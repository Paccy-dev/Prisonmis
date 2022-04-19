from django.contrib import admin
from .models import *

admin.site.register(Case)
admin.site.register(Prisoner)
admin.site.register(Visitor)
admin.site.register(Visit)
admin.site.register(Leave)

