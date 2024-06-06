from django.db import models


# Create your models here.
class FoodType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Taom turi')

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=150,verbose_name='Taom nomi')
    price = models.IntegerField(verbose_name='Taom narxi')
    ingidrients = models.TextField(null=True, verbose_name='Taom tarkibi')
    foodtype = models.ForeignKey(FoodType,on_delete=models.SET_NULL,null=True, verbose_name='taom turi')


    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(blank=True, null=True, verbose_name='Taom haqida izohingiz')
    created = models.CharField(max_length=150, verbose_name='Post qoldirilgan vaqt')
    author_name = models.CharField(max_length=150, verbose_name='Post muallifi')
    food_name = models.ForeignKey(Food, on_delete=models.SET_NULL, verbose_name='Taom nomi', null=True)


    def __str__(self):
        return self.author_name

