from django import forms

class CamionForm(forms.Form):
    P1 = forms.FloatField(label="Eje delantero (Ton)")
    P2 = forms.FloatField(label="Eje central (Ton)")
    P3 = forms.FloatField(label="Eje trasero (Ton)")
    L  = forms.FloatField(label="Luz de la viga (luz < 50 m.delta=0.2 m.) (m)")
    A  = forms.FloatField(label="DISTANCIA ENTRE EJES DELANTERO Y CENTRAL (m)")
    B  = forms.FloatField(label="DISTANCIA ENTRE EJES CENTRAL Y TRASERO (m)")
    PL = forms.FloatField(label="Distancia con Respecto a la posicion (m)", initial=0.2)
    Q  = forms.FloatField(label="Peso propio (Ton/m)")
