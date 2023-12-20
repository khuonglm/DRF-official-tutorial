from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

app_name = 'snippets'
urlpatterns = [
    path('', views.snippet_list, name='all'),
    path('<int:pk>/', views.snippet_detail, name='detail'),
]

# add .json, .api, .format after the api, example abc/snippets/ => abc/snippets/.json
urlpatterns = format_suffix_patterns(urlpatterns)