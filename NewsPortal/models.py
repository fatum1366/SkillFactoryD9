from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

class Author(models.Model):
    user_rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        author_posts_rating = Post.objects.filter(post_author_id=self.pk).aggregate(post_rating=Sum('post_rating'))[
            'post_rating']
        author_comments_rating = Comment.objects.filter(user_id=self.user).aggregate(comment_rating=Sum(
            'comment_rating'))['comment_rating']
        posts_comments_rating = Comment.objects.filter(post__post_author__user=self.user).aggregate(comment_rating=Sum(
            'comment_rating'))['comment_rating']
        self.user_rating = author_posts_rating * 3 + author_comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    category = models.CharField(unique=True, max_length=20)


article = 'AR'
news = 'NE'

POST_TYPES = [
        (article, 'Статья'),
        (news, 'Новость')
]


class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(choices=POST_TYPES, max_length=2)
    post_time = models.DateTimeField(auto_now_add=True)
    post_categories = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def preview(self):
        return self.post_text[:124] + '...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.post_title} {self.post_time: %d/%m/%y}: {self.post_text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
