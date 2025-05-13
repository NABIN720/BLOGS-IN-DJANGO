from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
# class blogPost(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     head = models.CharField(max_length=300)
#     content = models.CharField(max_length=3000)
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE,default='')
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)
#     slug = models.SlugField(unique=True, blank=True)
#     is_published = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['-created_at']
    
#     def save(self, *args, **kwargs):
#         # Automatically generate slug from title if not set
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         from django.urls import reverse
#         return reverse("blog_detail", kwargs={"slug": self.slug})
    
class bPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50,default='')
    head = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    head1 = models.CharField(max_length=100)
    content1 = models.CharField(max_length=3000)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,default='')
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='apk/images',default='')

    def __str__(self):
        return self.title