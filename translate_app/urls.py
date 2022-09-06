from django.urls import path
from . import views


app_name = 'translate_app'

urlpatterns = [
    path('history/',views.TranslateListView.as_view(),name='history'),
    path('home/',views.HomeView.as_view(),name='home'),
    path('detail/<int:pk>',views.TranslateDetailView.as_view(),name='detail'),
]
