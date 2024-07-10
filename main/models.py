from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Sarlavha' , max_length=255)
    task = models.TextField('Kengaytma')


    

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
