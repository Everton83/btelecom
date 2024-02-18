from django.urls import path
from .views import HomeView, SearchResultsView

app_name = "btelecomapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search_results/", SearchResultsView.as_view(), name="search_results"),
    # outras URLs aqui, se houver
]

