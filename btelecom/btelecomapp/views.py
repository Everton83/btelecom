from django.db.models.query_utils import select_related_descend
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from.models import *

# Create your views here.

class HomeView(ListView):
    template_name = "home.html"
    model = Solucoes
    context_object_name = 'home'
    paginate_by = 3
    queryset = Solucoes.objects.all()

class SearchResultsView(ListView):
    template_name = "search_results.html"
    model = Solucoes
    context_object_name = 'search_results'
    paginate_by = 3
    queryset = Solucoes.objects.all()
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Solucoes.objects.filter(
            Q(numero__icontains=query) | Q(portas__icontains=query) | Q(descricao__icontains=query )
        )
        return object_list