from django.contrib import admin

from apps.pizzamarket.models import CategoryFood, PublicationFood, CommentUser, ArticleTag, EmailUser


@admin.register(CategoryFood)
class CategoryFoodAdmin(admin.ModelAdmin):
    pass


@admin.register(PublicationFood)
class PublicationFoodAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentUser)
class CommentUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailUser)
class EmailUserAdmin(admin.ModelAdmin):
    pass