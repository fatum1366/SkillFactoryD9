from django.urls import path
from .views import PostList, PostDetail, NewsCreate, NewsUpdate, PostDelete, SearchList


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', SearchList.as_view(), name='post_search'),
   path('create/', NewsCreate.as_view(), name='create_news'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='update_news'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]