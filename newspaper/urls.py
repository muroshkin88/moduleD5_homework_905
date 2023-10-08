from allauth.account import views
from django.urls import path


from .views import PostsList, PostList # импортируем представление


urlpatterns = [
    path('', PostsList.as_view(), name='posts'), # т.к. это класс, представляем его в виде view, для этого вызываем метод as_view
    path('<int:pk>', PostList.as_view(), name='post'),  # pk — первичный ключ поста, который будет выводиться в шаблон

    path('signup/', views.signup, name='account_signup'),
    path('login/', views.login, name='account_login'),
    path('logout/', views.logout, name='account_logout'),
]

