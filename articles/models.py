from django.db import models
from django.conf import settings
from django.urls import reverse

# from news.django_project import articles

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ("article_detail", kwargs={"pk":self.pk})
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )
    def __str__(self):
        return self.comment
    
    def get_absulate_url(self):
        return reverse("article_list")