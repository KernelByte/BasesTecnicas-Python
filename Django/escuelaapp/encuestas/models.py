from django.db import models

# Create your models here.
class Question(models.Model):
    #Columnas de la tabla
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

class Choises(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)