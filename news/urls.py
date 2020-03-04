from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns =[
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^$', views.news_today, name = 'newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),  
]