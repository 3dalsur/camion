from django import forms

class CamionForm(forms.Form):
    P1 = forms.FloatField(label="Eje delantero (Ton)")
    P2 = forms.FloatField(label="Eje central (Ton)")
    P3 = forms.FloatField(label="Eje trasero (Ton)")
    L  = forms.FloatField(label="Luz de la viga (m)")
    A  = forms.FloatField(label="Distancia A (m)")
    B  = forms.FloatField(label="Distancia B (m)")
    PL = forms.FloatField(label="?x (m)", initial=0.2)
    Q  = forms.FloatField(label="Peso propio (Ton/m)")