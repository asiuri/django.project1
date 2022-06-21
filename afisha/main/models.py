from django.db import models
from datetime import date
# Create your models here.


class Movie(models.Model):
    """фильм"""
    object =None
    title = models.CharField("Название",max_length=100)
    description = models.TextField("Описание")
    image=models.ImageField(upload_to="images",verbose_name="photo")
   # directors=models.ManyToManyField(verbose_name="режиссор",related_name="film_director")
    #actors = models.ManyToManyField(verbose_name="актеры", related_name="film_actor")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фильм"
        verbose_name_plural = "фильм"

class Director(models.Model):
    name = models.CharField(max_length=200,default=0)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Отзывы и Коментари"
        verbose_name_plural = "Отзывы и Коментари"

class Review(models.Model):
    """Отзывы """
    name = models.CharField("Имя", max_length=100)
    email=models.EmailField()
    text = models.TextField(verbose_name="Сообщение" ,max_length=5000)
    parent=models.ForeignKey(
        'self',verbose_name="Родитель",on_delete=models.SET_NULL,blank=True,null=True
    )
    movie=models.ForeignKey(Movie,verbose_name="фильм",on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}-{self.movie}"

    class Meta:
        verbose_name = "Отзывы и "
        verbose_name_plural = "Отзывы "


class Actor(models.Model):
    """ Актеры и режиссеры"""
    name = models.CharField("Имя",max_length=100)
    age = models.PositiveIntegerField("Возрасть",default=0)
    image=models.ImageField("Изображение",upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Актеры и режиссеры"
        verbose_name_plural="Актеры и режиссеры"