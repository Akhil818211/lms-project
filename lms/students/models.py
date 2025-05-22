from django.db import models

# Create your models here.

from courses.models import BaseClass

class QualificcationChoices(models.TextChoices):

    MATRICULATION = 'Matriculation', 'Matriculation'
    POSTMATRICULATION = 'Postmatriculation', 'Postmatriculation'
    DIPLOMA = 'Diploma', 'Diploma'
    GRADUATION = 'Graduation', 'Graduation'
    POSTGRADUATION = 'Postgraduation', 'Postgraduation'
    PHD = 'PHD','PHD'
    

class Students(BaseClass):

    profile = models.ForeignKey('authentication.Profile',on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='students-image')

    qualification = models.CharField(max_length=50,choices=QualificcationChoices.choices)

    def __str__(self):
        return self.name
    
    class Meta :

        verbose_name = 'Students'

        verbose_name_plural = 'Students'

