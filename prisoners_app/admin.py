from django.contrib import admin
from .models import *

admin.site.register(Case)
admin.site.register(Prisoner)
admin.site.register(Visit)
admin.site.register(Leave)
admin.site.register(Complain)
admin.site.register(Reply)

