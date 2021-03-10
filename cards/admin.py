from django.contrib import admin
from .models import Set, Card, Reflection

# Register your models here.

admin.site.register(Card)
admin.site.register(Set)
admin.site.register(Reflection)