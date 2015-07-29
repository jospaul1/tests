from django.db import models
from django.utils import timezone
from django import VERSION as djangoVersion


def expensive_calculation():
    expensive_calculation.num_runs += 1
    return timezone.now()


class Poll(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
    if( djangoVersion[0:2] >= ( 1, 8 ) ):
        expensive_calculation.num_runs=0
    
    pub_date = models.DateTimeField('date published', default=expensive_calculation)
