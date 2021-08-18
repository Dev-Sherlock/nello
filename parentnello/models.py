from django.db import models


# Create your models here.

class Content(models.Model):
    text = models.TextField(editable=True, blank=True)
    image = models.ImageField(editable=True, blank=True)
    video = models.FileField(upload_to='videos/',blank=True)

    class Meta:
        verbose_name = 'content'
        verbose_name_plural = 'contents'

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.CharField(max_length=300,blank=True)
    comment = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    def __str__(self):
        return self.author


class Post(models.Model):
    title = models.CharField(max_length=200)
    nsfw = models.BooleanField(default=False, blank=True)
    creation_date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=300)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE,blank=True,null=True)
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        # primary_key=True,
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    def __str__(self):
        return self.title

