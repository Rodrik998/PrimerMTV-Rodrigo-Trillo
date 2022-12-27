from django.db import models

class family(models.Model):
    name = models.CharField(max_length = 100)
    DNI = models.FloatField()
    use_glases = models.BooleanField()
