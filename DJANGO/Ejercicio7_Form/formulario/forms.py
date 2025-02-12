from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Tu nombre"}),label="Nombre")
    AFICIONES_CHOICES = [
        ('conducir', 'Conducir'),
        ('futbol', 'Futbol'),
        ('padel', 'Padel'),
        ('videojuegos', 'Videojuegos'),
        ('cocinar', 'Cocinar'),
    ]
    
    aficiones = forms.MultipleChoiceField(
        choices=AFICIONES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),  # Estilo para los checkboxes
        required=False,  # Permite no seleccionar nada si lo deseas
        label="Lenguajes de Programación"
    )