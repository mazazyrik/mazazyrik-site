from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('stack', views.StackView.as_view(), name='stack'),
     path('story', views.StoryView.as_view(), name='story'),
     path('contact', views.contact, name='contact')
]
