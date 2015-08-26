from django.db import models

# Create your models here.

class UserDetails(models.Model):
    url = models.URLField()
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    photo = models.URLField(blank=True)

    def __str__(self):
            return self.user.username

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Detail'