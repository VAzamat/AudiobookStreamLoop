from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID жанра")
    uuid = models.UUIDField(verbose_name="UUID жанра")
    name = models.CharField(max_length=255, verbose_name="Название жанров")
    is_root = models.BooleanField(default=False, verbose_name="Корневой ли?")
    url = models.CharField(max_length=255, verbose_name="URL жанра")
    is_main = models.BooleanField(default=False, verbose_name="Основной ли?")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self): return self.name

class Publisher(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID издательства")
    name = models.CharField(max_length=255, verbose_name="Название издательства")
    url = models.CharField(max_length=255, verbose_name="URL издательства", blank=True, null=True)

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self): return self.name

class Copyrighter(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID копирайтера", blank=True)
    name = models.CharField(max_length=255, verbose_name="Название копирайтера")
    url = models.CharField(max_length=255, verbose_name="URL", blank=True, null=True)

    class Meta:
        verbose_name = "Копирайтер"
        verbose_name_plural = "Копирайтеры"

    def __str__(self): return self.name


class Rightholder(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID правообладателя")
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="URL", blank=True, null=True)

    class Meta:
        verbose_name = "Правообладатель"
        verbose_name_plural = "Правообладатели"

    def __str__(self): return self.name

class Rating(models.Model):
    user_rating = models.FloatField(null=True, blank=True, verbose_name="Рейтинг книги")
    rated_1_count = models.IntegerField(default=0, verbose_name="Кол-во оценок '1'")
    rated_2_count = models.IntegerField(default=0, verbose_name="Кол-во оценок '2'")
    rated_3_count = models.IntegerField(default=0, verbose_name="Кол-во оценок '3'")
    rated_4_count = models.IntegerField(default=0, verbose_name="Кол-во оценок '4'")
    rated_5_count = models.IntegerField(default=0, verbose_name="Кол-во оценок '5'")
    rated_avg = models.FloatField(verbose_name="Средний рейтинг")
    rated_total_count = models.IntegerField(verbose_name="Общее кол-во оценок")

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return f"Avg: {self.rated_avg} ({self.rated_total_count} votes)"
