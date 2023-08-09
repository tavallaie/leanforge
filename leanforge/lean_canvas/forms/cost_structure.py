from django import forms
from lean_canvas.models import CostStructure


class CostStructureForm(forms.ModelForm):
    class Meta:
        model = CostStructure
        fields = ["cost"]
