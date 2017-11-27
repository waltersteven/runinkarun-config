from django import forms
from .models import Partida

class PartidaForm(forms.ModelForm):
    
    escenario = forms.MultipleChoiceField(choices=Partida.ESCENARIO_CHOICES, widget=forms.CheckboxSelectMultiple)
    personaje = forms.MultipleChoiceField(choices=Partida.PERSONAJE_CHOICES, widget=forms.CheckboxSelectMultiple)
    modo_juego = forms.MultipleChoiceField(choices=Partida.GAME_MODE_CHOICES, widget=forms.CheckboxSelectMultiple)
    dificultad = forms.MultipleChoiceField(choices=Partida.DIFICULTAD_CHOICES, widget=forms.CheckboxSelectMultiple)

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
            # 'game_time',
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
            # 'game_time': 'Tiempo de juego (seg)',
            'musica': 'Musica de fondo',               
        }

        widgets = {
            'intro_background': forms.Select(attrs={'class': 'form-control'}),
            'speed_player': forms.NumberInput(attrs={'style': 'border-radius: 4px', 'min': 1, 'max':5}),
            'life': forms.NumberInput(attrs={'style': 'border-radius: 4px', 'min': 1, 'max':5}),
            # 'game_time': forms.NumberInput(attrs={'style': 'border-radius: 4px', 'min': 15, 'max':100}),
            'musica': forms.Select(attrs={'class': 'form-control'}),
        }