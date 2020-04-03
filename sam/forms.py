from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    """I don't really know what i'm doing"""

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)


        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })


    class Meta:
        model = Client
        fields = ("__all__")