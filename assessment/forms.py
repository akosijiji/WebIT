from django import forms  
from .models import Client  

class ClientForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['client_name'].required = True
        self.fields['phone_number'].required = True
        self.fields['email_address'].required = True
        self.fields['street_name'].required = False
        self.fields['suburb'].required = False
        self.fields['postcode'].required = False
        self.fields['state'].required = False
        self.fields['contact_name'].required = False

    class Meta:  
        model = Client
        fields = "__all__"   