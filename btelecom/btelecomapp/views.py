from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from .models import Solucoes

class HomeView(ListView):
    template_name = "home.html"
    model = Solucoes
    context_object_name = 'home'
    paginate_by = 8
    queryset = Solucoes.objects.all().order_by('id')

class SearchResultsView(ListView):
    template_name = "search_results.html"
    model = Solucoes
    context_object_name = 'search_results'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Solucoes.objects.filter(
                Q(numero__icontains=query) | Q(portas__icontains=query) | Q(descricao__icontains=query)
            ).order_by('id')  # Ordem por ID para garantir consistência na paginação
        else:
            return Solucoes.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Quantidade de páginas para mostrar na paginação
        max_index = len(paginator.page_range)
        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index
        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context
