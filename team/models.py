from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    photo = models.ImageField(upload_to='team_photo', verbose_name="Фото працівника")

    def __str__(self):
        return self.name




