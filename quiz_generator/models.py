from django.db import models

class Question(models.Model):
    question_string = models.TextField()
    answer = models.TextField()
    category = models.TextField()
    question_ID = models.IntegerField()

    def __str__(self):
        return self.question_string