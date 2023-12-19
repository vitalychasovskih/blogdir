from django.db import models


class BlogPost(models.Model):
    """Пост, который может добавить пользователь"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns a string representation of the model"""
        return self.title