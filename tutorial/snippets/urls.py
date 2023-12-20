from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

app_name = 'snippets'
urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippets_list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippets_detail'),
    path('users/', views.UserList.as_view(), name='users_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users_detail'),
]

# add .json, .api, .format after the api, example abc/snippets/ => abc/snippets/.json
urlpatterns = format_suffix_patterns(urlpatterns)