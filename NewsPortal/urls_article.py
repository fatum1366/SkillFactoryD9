from django.urls import path
from .views import PostList, ArticleCreate, ArticleUpdate, PostDelete

urlpatterns = [

    path('', PostList.as_view(), name='article_list'),

    path('create/', ArticleCreate.as_view(), name='create_article'),

    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='update_article'),

    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]