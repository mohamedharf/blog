from django.db import models
#import user
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to="blog-images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    
    
    def get_related_post_by_tag(self):
        return Blog.objects.filter(tags__in=self.tags.all()).distinct()[1:4]
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
     return reverse('detail', kwargs={'pk': self.pk})  
 
 #coment
class Coment(models.Model):
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    crated_at=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username