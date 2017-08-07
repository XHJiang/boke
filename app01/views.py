from django.shortcuts import render, HttpResponse

from app01 import models

def hello(request):
    return HttpResponse('hello world')


def article(request, *args, **kwargs):
    print(kwargs)
    # print(request.path_info)
    #
    # from django.urls import reverse
    # url = reverse('article', kwargs=kwargs)
    # # url = reverse('article',kwargs={'article_type_id': '1', 'category_id': '1'})
    # print(url)

    condition = {}
    for k,v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            condition[k] = v

    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()

    # result = models.Article.objects.all()
    result = models.Article.objects.filter(**condition)
    return render(
        request,
        'article.html',
        {
            'result': result,
            'article_type_list': article_type_list,
            'category_list': category_list,
            'kwargs': kwargs,
        }
    )