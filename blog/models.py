from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

#1:N

# class Article(models.Model):
#     title = models.CharField(max_length=20)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     published_at = models.DateTimeField(null=False)

#     def __str__(self):
#         return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text