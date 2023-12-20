from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

app_name = 'snippets'
urlpatterns = [
    path('', views.SnippetList.as_view(), name='list'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name='detail'),
]

# add .json, .api, .format after the api, example abc/snippets/ => abc/snippets/.json
urlpatterns = format_suffix_patterns(urlpatterns)