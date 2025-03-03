from django.db import models

# Create your models here.

class HeartRate(models.Model):
    user = models.CharField(max_length=50)
    bpm = models.IntegerField() # Beats per min
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User {self.user_id}: {self.bpm} BPM'