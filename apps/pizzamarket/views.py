from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic

from apps.pizzamarket.models import PublicationFood, CategoryFood, CommentUser, EmailUser
import django_rq
from apps.pizzamarket.forms import CommentUserForm


class FoodsListView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'publication_list'

    def get_queryset(self):
        query_params = self.request.GET
        search_word = query_params.get('search_word')
        category_id = query_params.get('category_pk')
        publication_qs = PublicationFood.objects.all()
        if search_word:
            publication_qs = publication_qs.filter(name__contains=search_word)
        if category_id:
            try:
                category_id = int(category_id)
            except ValueError:
                pass
            else:
                publication_qs = publication_qs.filter(category_id=category_id)
        return publication_qs


class FoodsDetailView(generic.DetailView):
    template_name = 'blog-single.html'
    context_object_name = 'publication'
    model = PublicationFood
    slug_field = 'id'
    slug_url_kwarg = 'pub_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FoodsDetailView, self).get_context_data(**kwargs)
        context['category_list'] = CategoryFood.objects.all()
        return context


class MenuView(generic.TemplateView):
    template_name = 'menu.html'
    # context_object_name = 'publication_list'
    # model = PublicationFood

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['publication_list'] = PublicationFood.objects.all()
        return context


queue = django_rq.get_queue('default')


def send_mail_task(user_email:str):
    send_mail(
        'вам пришло новое сообщения',
        'спасибо за оставленный комментарий',
    settings.EMAIL_HOST_USER,
    [user_email],
    fail_silently = True
    )


def add_comment_publication(request, pk):#запрос
    if request.method == 'POST': #запрос
        post_request_data = request.POST
        comment_form = CommentUserForm(post_request_data)
        print('здесь значение рекуест пост ', request.POST)  #запрос
        if comment_form.is_valid():
            comment=CommentUser.objects.create(
                text=comment_form.data['text'],
                name=comment_form.data['name'],
                email=comment_form.data['email'],
                category_id=pk)
            if comment.user_email:
                queue.enqueue(send_mail_task, user_email=comment.user_email)
                    # 'вам пришло новое сообщения',
                    # 'спасибо за оставленный комментарий',
                    # settings.EMAIL_HOST_USER,
                    # [comment.user_email],
                    # fail_silently=True)

            return HttpResponse(content='каментарий успешно добавлен.')
        else:
            return HttpResponse(content=f'покоже вы не правильно заполнили форму:{comment_form.errors}')




