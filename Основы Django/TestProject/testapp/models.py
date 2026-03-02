from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title=models.CharField(
        max_length=200,
        unique=True,
        db_index=True
    )
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    is_published=models.BooleanField(default=False)

    STATUS_CHOICES = [
        ("draft","Черновик"),
        ("published","Опубликовано"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="",
    )

    # One to Many
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        #CASCADE, PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING
        related_name="posts"
    )

    # Many to Many
    tags = models.ManyToManyField(
        "Tag",
        related_name="posts",
        blank=True
    )
   
    def __str__(self):
        return f"{self.author} - {self.title}"

    def increment_views(self):
        self.view_count+=1
        self.save()
    
    class Meta:
        # ordering = ["-created_at"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        # unique_together = ("title","author")

class Tag(models.Model):
    name=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name