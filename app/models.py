"""
Definition of models.
"""

from django.db import models
from django import forms

# Create your models 
class Artist(models.Model):
    name = models.CharField(max_length=50)
    year_Formed = models.PositiveIntegerField()
    
class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist)

class artistForm(forms.ModelForm):
    class Meta:
        model = Artist;
        fields = ['name' , 'year_Formed'];