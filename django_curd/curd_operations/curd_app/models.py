from django.db import models

# Create your models here.

class CurdOperations(models.Model):

    first_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    #dob = models.DateField()
    
    def __str__(self):
        return self.first_name
