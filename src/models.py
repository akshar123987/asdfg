from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model): #models.model means inherit model present in models package.
    title = models.CharField(max_length=60)    #charfield etc present in Model
    published_at = models.DateTimeField()
    description = models.TextField()
    author_name = models.CharField(max_length=20) # charfield used to limit the input

    def __str__(self):
        return self.title

class  Comment(models.Model):
    post = models.ForeignKey(Post)
    description = models.TextField()
    published_at = models.DateTimeField(default=timezone.now())