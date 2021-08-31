from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import constraints
from django.db.models.constraints import UniqueConstraint

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"
    def __str__(self):
        return self.username
class Habit(models.Model):
    title = models.CharField(max_length=250)
    goal = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits"
    )

    def __str__(self):
        return f'{self.title}'

class DailyRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="records")

    #class Meta:
     #   constraint = models.UniqueConstraint(
      #      fields=['habit', 'date'], name='unique_record')
    
    #def __repr__(self):
    #    return f"<Daily Record date={self.date}>"

    #def __str__(self):
    #    return f"{self.date}"
    
