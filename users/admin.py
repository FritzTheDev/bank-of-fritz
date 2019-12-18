from django.contrib.admin import ModelAdmin, register
from .models import User

# Register your models here.
@register(User)
class UserAdmin(ModelAdmin):
  pass