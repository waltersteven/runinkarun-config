import json
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Partida
from .forms import PartidaForm
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from .serializers import PartidaSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status


# Create your views here (Class based view).
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

class PartidaAPI(APIView):
    serializer = PartidaSerializer

    def get(self, request, format=None):
        lista = Partida.objects.all()
        response = self.serializer(lista, many=True)
        return Response(response.data)
        # return HttpResponse(json.dumps(response.data), content_type='application/json')
        

    def post(self, request, format=None):
        partidita = self.serializer(data=request.data)
        if partidita.is_valid():
            partidita.save()
            return Response(partidita.data, status=status.HTTP_201_CREATED)
        return Response(partidita.errors, status=status.HTTP_400_BAD_REQUEST)