from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# from tinymce import HTMLField
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class AboutUs(models.Model):
    title = models.CharField(unique=True,max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(unique=True,max_length=100)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post:category", args=[self.slug])
    
    
    

class Post(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True)
    postText = models.TextField() 
    photo = models.ImageField(upload_to = 'photos', default="default.png", blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=False)
    date_updated = models.DateTimeField(default=timezone.now, null=False)
    
    def get_thumnail(self):
        if self.photo:
            return self.photo.url
        return ''
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse("post:blog-detail", kwargs={"slug": self.slug})
        # return reverse("post:blog-detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    