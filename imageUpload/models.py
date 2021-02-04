from django.db import models

class Post(models.Model):
   text = models.CharField(max_length=500)
   location = models.CharField(max_length=100)
class PostImage(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   image = models.ImageField(upload_to="post/%Y/%m/%d")
   def __str__(self):
       return '[{}] {}'.format(self.post, self.image)