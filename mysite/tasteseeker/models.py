from django.db import models
from django.forms import ModelForm

CHOICE_TYPE = [
    ('Gin', 'Gin'),
    ('Vodka', 'Vodka'),
    ('Rum', 'Rum'),
    ('Tequila', 'Tequila'),
    ('Whiskey', 'Whiskey'),
]

class Cocktail(models.Model):
    Type = models.CharField(max_length=60, choices=CHOICE_TYPE)
    CocktailName = models.CharField(max_length=60, default="", blank=True, null=False)
    Bar_or_Restaurant = models.CharField(max_length=60, default="", blank=True, null=False)
    City = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Description = models.CharField(max_length=300, default="", blank=True, null=False)
    User = models.CharField(max_length=60, default="", blank=True, null=False)
    Price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True, )

    objects = models.Manager()



    def __str__(self):
        return self.CocktailName