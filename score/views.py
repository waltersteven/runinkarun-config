from django.shortcuts import render
from .models import Score
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScoreSerializer

# Create your views here.
class ScoreAPI(APIView):
    serializer = ScoreSerializer

    def get(self, request, format=None):
        score = Score.objects.all()
        response = self.serializer(score, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        score = self.serializer(data=request.data)
        if score.is_valid():
            score.save()
            return Response(score.data, status=status.HTTP_201_CREATED)
        return Response(score.data, status=status.HTTP_400_BAD_REQUEST)

class ScoreList(ListView):
    model = Score
    template_name = 'score/index.html'