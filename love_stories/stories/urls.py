from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('stories/',views.stories,name='nice_stories'),
    path('add_story/',views.add_story,name='add_story'),
    path('about/',views.about,name='about'),
]
