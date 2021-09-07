from django.db import models
from django.urls import reverse
    

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', related_name='projects',
                               on_delete=models.CASCADE)
    
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])