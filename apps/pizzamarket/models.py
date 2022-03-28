from django.db import models
from ckeditor.fields import RichTextField


class CategoryFood(models.Model):
    name = models.CharField(max_length=200,unique=True)

    class Meta:
        verbose_name='категория'
        verbose_name_plural='категории'

    def __str__(self):
        return self.name


class ArticleTag(models.Model):

    name = models.CharField(max_length=255, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'

    def __str__(self):
        return self.name


class PublicationFood(models.Model):
    category=models.ForeignKey(to=CategoryFood,null=True, on_delete=models.SET_NULL,related_name='publication_set')
    name = models.CharField(max_length=250)
    description= RichTextField(max_length=500)
    poster=models.ImageField(upload_to='publication_images',null=True)
    created_at=models.DateTimeField(null=True)
    tags = models.ManyToManyField(to=ArticleTag, related_name='articles')


    class Meta:
        verbose_name='публикация'
        verbose_name_plural='Публикации'

    def __str__(self):
        return self.name


class CommentUser(models.Model):
    category = models.ForeignKey(to=PublicationFood, on_delete=models.CASCADE, related_name='comments')
    text=models.TextField(default='')
    user_name=models.CharField(max_length=100,default='')
    user_email=models.EmailField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='каментария'
        verbose_name_plural='каментарии'

    def __str__(self):
        return f'Комментарий для публикации с id:{self.category_id}'


class EmailUser(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()


    class Meta:
        verbose_name='пользаватель'
        verbose_name_plural='пользаватели'

    def __str__(self):
        return self.name

