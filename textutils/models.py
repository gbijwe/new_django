from django.db import models

class team(models.Model):
    team_name = models.CharField(max_length=40)
    class Meta:
        app_label = 'textutils'

    TEAM_LEVELS = (
        ('U09', 'Under 09s'),
        ('U10', 'Under 10s'), 
        ('U11', 'Under 11s')
    )

    team_level = models.CharField(max_length=3, choices=TEAM_LEVELS, default='U11')