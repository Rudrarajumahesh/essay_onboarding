from django.db import models

# Create your models here.
import random

class Essay(models.Model):
    student_id = models.CharField(max_length=100)
    college_name = models.CharField(max_length=255)
    question_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class EssayVersion(models.Model):
    essay = models.ForeignKey(Essay, on_delete=models.CASCADE, related_name='versions')
    content = models.FileField(upload_to='essays/')
    scorecard = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.scorecard:
            self.scorecard = {
                'structure': random.randint(1, 5),
                'clarity': random.randint(1, 5),
                'impact': random.randint(1, 5),
            }
        super().save(*args, **kwargs)