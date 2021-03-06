from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Partida(models.Model):

    def __str__(self):
        return '{}'.format(self.game_time)

    WARI = 'WAR'
    MOCHICA = 'MOC'
    PARACAS = 'PAR'
    TIAHUANACO = 'TIA'

    ESCENARIO_CHOICES = (
        (WARI, 'Wari'),
        (MOCHICA, 'Mochica'),
        (PARACAS, 'Paracas'),
        (TIAHUANACO, 'Tiahuanaco'),
    )

    INCA_WARI = 'inwar'
    INCA_MOCHICA = 'inmoc'
    INCA_PARACAS = 'inpar'
    INCA_TIAHUANACO = 'intia'

    PERSONAJE_CHOICES = (
        (INCA_WARI, 'Inca Wari'),
        (INCA_MOCHICA,'Inca Mochica'),
        (INCA_PARACAS, 'Inca Paracas (Mujer)'),
        (INCA_TIAHUANACO, 'Inca Tiahuanaco'),
    )

    SINGLE = 'single'
    ARCADE = 'arcade'

    GAME_MODE_CHOICES = (
        (SINGLE, 'Single'),
        (ARCADE, 'Arcade'),
    )

    NORMAL = 'normal'
    DIFICIL = 'dificil'
    EXPERTO = 'experto'

    DIFICULTAD_CHOICES = (
        (NORMAL, 'Normal'),
        (DIFICIL, 'Dificil'),
        (EXPERTO, 'Experto'),
    )

    BACKGROUND_1 = 'http://res.cloudinary.com/dfktnvqxe/image/upload/v1511719844/escenario_fondo_v2_ikkq4e.jpg'
    BACKGROUND_2 = 'http://www.powerpointhintergrund.com/uploads/2017/05/simple-backgrounds-wallpaper-1920x1080--47273-24.jpeg'

    BACKGROUND_CHOICES = (
        (BACKGROUND_1, '1er background'),
        (BACKGROUND_2, '2do background'),
    )

    TRACK_1 = '1'
    TRACK_2 = '2'

    TRACK_CHOICES = (
        (TRACK_1, '1er track'),
        (TRACK_2, '2do track'),
    )

    escenario = models.CharField(max_length=200, blank = True, null = True)
    personaje = models.CharField(max_length=200, blank = True, null = True)
    modo_juego = models.CharField(max_length=200, blank = True, null = True)
    dificultad = models.CharField(max_length=200, blank = True, null = True)
    intro_background = models.CharField(max_length=250, choices=BACKGROUND_CHOICES, default=BACKGROUND_1,)
    speed_player = models.IntegerField(default=1)
    life = models.IntegerField(default=3)
    # game_time = models.IntegerField(default=500)
    musica = models.CharField(max_length=4, choices=TRACK_CHOICES, default=TRACK_1,)