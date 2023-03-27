from django.db import models


# Create your models here.
class Blog(models.Model):
    title =models.CharField(max_length=20)
    published_on=models.DateTimeField()
    author=models.CharField(max_length=44)
    description=models.TextField()
    is_published= models.BooleanField(default=False)

    class Meta:
        permissions=[('can_publish','Can Publish blog')]
        





