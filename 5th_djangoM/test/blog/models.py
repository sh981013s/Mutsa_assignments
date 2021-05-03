from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 20)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    introducing = models.TextField()

    def __str__(self):
        return self.title

