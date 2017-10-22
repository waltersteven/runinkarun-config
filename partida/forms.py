from django import forms
from .models import Partida

class PartidaForm(forms.ModelForm):

    class Meta:
        model = Partida
        fields = [
            'escenario',
            'personaje',
            'modo_juego',
            'dificultad',
            'intro_background',
            'speed_player',
            'life',
            'game_time',
            'musica',
        ]
        labels = {
            'escenario': 'Escenario',
            'personaje': 'Personaje',
            'modo_juego': 'Modalidad de juego',
            'dificultad': 'Dificultad',
            'intro_background': 'Imagen de background',
            'speed_player': 'Velocidad del jugador',
            'life': 'Cantidad de vidas',
            'game_time': 'Tiempo de juego (seg)',
            'musica': 'Musica de fondo',
        }
        widgets = {
            'escenario': forms.CheckboxSelectMultiple(),
            'personaje': forms.CheckboxSelectMultiple(),
            'modo_juego': forms.CheckboxSelectMultiple(),
            'dificultad': forms.CheckboxSelectMultiple(),
            'intro_background': forms.Select(attrs={'class': 'form-control'}),
            'speed_player': forms.NumberInput(attrs={'style': 'border-radius: 4px'}),
            'life': forms.NumberInput(attrs={'style': 'border-radius: 4px'}),
            'game_time': forms.NumberInput(attrs={'style': 'border-radius: 4px'}),
            'musica': forms.Select(attrs={'class': 'form-control'}),
        }