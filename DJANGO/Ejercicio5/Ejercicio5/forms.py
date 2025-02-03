from django import forms

class Formulario(forms.Form):
    aceptar=forms.BooleanField(required=True,label="Añadir",widget=forms.CheckboxInput)
