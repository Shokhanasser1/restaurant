from django.contrib import admin
from django.apps import apps
from .models import Dish
# Register your models here.
app = apps.get_app_config('menu')

for model_name, model in app.models.items():
    admin.site.register(model)
    