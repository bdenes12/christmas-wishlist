from django import forms

from .models import Gift


class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ["family_member", "name", "link"]
        labels = {
            "family_member": "Ki vagy te?",
            "name": "Mit szeretnél karácsonyra?",
            "link": "Link (opcionális)",
        }
