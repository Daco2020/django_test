# Create your models here.

from django.db import models
# python sell 클래스 호출.
# from products.models import Menu, Categories, Drinks, Allergy_drink, Images, Allergy 



class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'


class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Drinks(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=45, null=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'drinks'


class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'


class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    # on_delete 란 모델이 삭제되면 수행해야 할 작업을 의미함.
    # CASCADE: 참조 된 오브젝트가 삭제되면 해당 오브젝트를 참조하는 오브젝트도 삭제하십시오 (예를 들어 블로그 게시물을 제거 할 때 주석도 삭제하려고 할 수 있음). SQL에 상응하는 내용 : CASCADE.
    
    class Meta:
        db_table = 'images'


