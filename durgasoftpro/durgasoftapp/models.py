from django.db import models

# Create your models here.

# contact model
# services model
# feedback model


class ServicesData(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100, unique=True)
    course_duration = models.CharField(max_length=100)
    course_start_date = models.DateField(max_length=100)
    course_start_time = models.TimeField(max_length=100)
    course_trainer_name = models.CharField(max_length=100)
    course_trainer_exp = models.CharField(max_length=100)

# feedback model file here
class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField(max_length=100)
    feedback = models.CharField(max_length=100)