from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Published"))


class Plant(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    PLANT_LEVEL_CHOICES = [
        ("1", "Super hearty (it will survive anyone!)"),
        ("2", "Needs minor super vision, like a young adult"),
        ("3", "Must be checked up on at least once a week"),
        ("4", "Fussy, needs constant attention"),
    ]

    plant_level = models.CharField(
        max_length=250,
        choices=PLANT_LEVEL_CHOICES,
        default="1",
        null=False
    )

    PLANT_LIGHT_CHOICES = [
        ("BRIGHT", "Bright, indirect light required"),
        ("DIRECT", "Direct light required"),
        ("LOW", "Low light required"),
        ("MEDIUM", "Medium light required"),
    ]

    plant_light = models.CharField(
        max_length=250,
        choices=PLANT_LIGHT_CHOICES,
        default="1",
        null=False
    )

    plant_thirst = models.DecimalField(
        null=True,
        decimal_places=1,
        max_digits=3,
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
