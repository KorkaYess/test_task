from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from softdelete.models import SoftDeleteObject


class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=255, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Like(SoftDeleteObject, models.Model):

    class LikeOrNor(models.IntegerChoices):
        LIKE = 1
        DISLIKE = 0

    value = models.IntegerField(choices=LikeOrNor.choices)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE, editable=False)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return f'{self.user.username}  {self.like_or_dislike()}  {self.post}'

    def like_or_dislike(self):
        if self.value == 1:
            return 'Like'
        else:
            return "Dislike"