from django.db import models

# Create your models here.


# 测试git
class Category(models.Model):
    caption = models.CharField(max_length=16)


class ArticleType(models.Model):
    caption = models.CharField(max_length=16)


class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)

    category = models.ForeignKey(Category)
    article_type = models.ForeignKey(ArticleType)


    # type_choise = (
    #     (0,'Python')
    #     (1,'OpenSteck'),
    #     (2,'Linux'),
    # )
    # article_type_id = models.IntegerField(choices=type_choise)
