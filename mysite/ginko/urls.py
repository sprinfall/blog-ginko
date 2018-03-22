from django.urls import path

from . import views

# Namespace for URLconf.
# Django needs this to know which app view to create for a url when using
# the {% url %} template tag.
app_name = "ginko"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
