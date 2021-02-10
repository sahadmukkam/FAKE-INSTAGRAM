from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def liked_users(self):
        objects=Like.objects.filter(post=self).values_list('user',flat=True)
        return objects

class Like(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='user_likes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_likes')
    class Meta:
        unique_together= ['user','post']
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='user_comment')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comment')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Friends(models.Model):
    followers = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='followers')
    following = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='following')
    class Meta:
        unique_together = ['followers','following']
# Create your models here.
