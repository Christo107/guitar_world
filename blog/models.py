from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = models.ImageField('blog_image', default='placeholder')
    alt_tag = models.CharField(max_length=50, default='blogimage')
    excerpt = models.TextField(max_length=200, blank=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title
