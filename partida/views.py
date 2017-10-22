from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Partida
from .forms import PartidaForm
from django.core.urlresolvers import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'partida/index.html')


class PartidaList(ListView):
    model = Partida
    template_name = 'partida/partida_list.html'


class PartidaCreate(CreateView):
    model = Partida
    form_class = PartidaForm
    template_name = 'partida/partida_form.html'
    success_url = reverse_lazy('partida:partida_listar')

class PartidaUpdate(UpdateView):
    model = Partida
    form_class = PartidaForm
    template_name = 'partida/partida_form.html'
    success_url = reverse_lazy('partida:partida_listar')

class PartidaDelete(DeleteView):
    model = Partida
    template_name = 'partida/partida_delete.html'
    success_url = reverse_lazy('partida:partida_listar')