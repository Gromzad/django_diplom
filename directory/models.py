from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True, upload_to='images/category/', verbose_name='Зображення категорії')

    class Meta:
        verbose_name_plural = "категорії"

    def __str__(self):
        return self.title

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True, upload_to='images/items', verbose_name='Зображення виробу')

    @property
    def href(self):
        """Returns the item's href name."""
        if self.category.title == "Вироби металургійного виробництва":
            return "metalproduction"
        elif self.category.title == "Вироби машинобудівного виробництва":
            return "machinebuild"
        elif self.category.title == 'Вироби інструментального виробництва':
            return 'instrproduction'
        elif self.category.title == 'Вироби автомобілебудівного виробництва':
            return 'carbuild'
        elif self.category.title == 'Вироби тракторного та сільсьскогосподарського машинобудування':
            return 'traktorbuild'
        elif self.category.title == 'Вироби хімічного машинобудування':
            return 'chembuild'

    class Meta:
        verbose_name_plural = "Вироби"

    def __str__(self):
        return self.title





