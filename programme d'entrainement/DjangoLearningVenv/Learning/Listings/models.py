# listings/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    def __str__(self):
            return f'{self.name}'
    
    class Genre(models.TextChoices):
            HIP_HOP = 'HH'
            SYNTH_POP = 'SP'
            ALTERNATIVE_ROCK = 'AR'

    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
   

class Listings(models.Model):
    class Type(models.TextChoices):
        Records = "rc"
        Clothing = "Ct"
        Posters = "Pt"
        Miscellaneous = "Mn"
    
    title = models.fields.CharField(max_length=1000, default='')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    description = models.fields.TextField(max_length="255", default='')
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(default=2000, validators=[
        MinValueValidator(1900), MaxValueValidator(2021)])
    type = models.CharField(choices = Type.choices, max_length=5)
    
    