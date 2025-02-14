from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tu nombre"}),
        label="Nombre"
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Tu email"}),
        label="Email",
        error_messages={
            'invalid': 'Por favor ingresa un correo electrónico válido.',
        }
    )

    edad = forms.IntegerField(
        required=True,
        min_value=17, #se puede validar la edad aqui
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Tu edad"}),
        label="Edad",
        error_messages={
            'min_value': 'Debes tener al menos 16 años para registrarte.'
        }
    )

    SEXO_CHOICES = [
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ]

    sexo = forms.MultipleChoiceField(
        choices=SEXO_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True,
        label="Sexo"
    )

    AFICIONES_CHOICES = [
        ('conducir', 'Conducir'),
        ('futbol', 'Fútbol'),
        ('padel', 'Pádel'),
        ('videojuegos', 'Videojuegos'),
        ('cocinar', 'Cocinar'),
    ]

    aficiones = forms.MultipleChoiceField(
        choices=AFICIONES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label="Aficiones"
    )

    TEMAS_INTERES_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('csharp', 'C#'),
        ('php', 'PHP'),
    ]

    temas_interes = forms.ChoiceField(
        choices=TEMAS_INTERES_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label="Temas de Interés en Programación"
    )
