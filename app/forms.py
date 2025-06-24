from django import forms
from app.models import Actores

class ActoresForm(forms.ModelForm):
    class Meta:
        model = Actores
        fields = '__all__'

        # Usamos este widget para dar al usuario una ayuda al ingresar la fecha
        widgets = {
            'ActorId': forms.NumberInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'FechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # ¡Aquí está la clave!
            'Biografia': forms.TextInput(attrs={'class': 'form-control'}),
        }
