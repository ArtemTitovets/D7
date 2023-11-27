from django.urls import path
from .views import (PostList, PostDetail, PostSearch, ArticlesCreate, ArticlesUpdate, ArticlesDelete,
                    NewsCreate, NewsUpdate, NewsDelete)

urlpatterns = [
   path('', PostList.as_view(),name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('search/', PostSearch.as_view(), name='news_search'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]