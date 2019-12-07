#pip install django-multiselectfield
#Model.py
from django.db import models
from multiselectfield import MultiSelectField
class Framework(models.Model):
   FRAMEWORK_PYTHON=(
        ('Kivy','Kivy'),
        ('sanic','Sanic'),
        ('Flask','Flask'),
        ('Django','Django')
    )
    framework=MultiSelectField( choices=FRAMEWORK_PYTHON)
#Forms.py

#admin.py
from .models import Framework

admin.site.register(Framework)

#settings.py
INSTALLED_APP=[
   ' multiselectfield'
]
#########OR METHOD#################
#Model.py
from django.db import models

FRAMEWORK_PYTHON = (
    ('Kivy', 'Kivy'),
    ('sanic', 'Sanic'),
    ('Flask', 'Flask'),
    ('Django', 'Django')
)
class Framework(models.Model):

    framework = models.CharField(max_length=100,choices=FRAMEWORK_PYTHON,default='Django')

#Forms.py
FRAMEWORK_PYTHON = (
    ('Kivy', 'Kivy'),
    ('sanic', 'Sanic'),
    ('Flask', 'Flask'),
    ('Django', 'Django')
)

class Framework(forms.ModelForm):
    framework = forms.CharField(max_length=100, choices=FRAMEWORK_PYTHON, default='Django')


