from django import forms
from .models import ContactForm
import re

class ContactDjangoForms(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'telephone', 'message']
        error_messages = {
            "name": {"required": "* Informe seu nome"},
            "email": {
                "required": "* Informe seu email",
                "invalid": "* Digite um email válido"
            },
            "message": {"required": "* Digite uma mensagem"}
        }
    
    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise forms.ValidationError("* Nome precisa ter pelo menos 3 caracteres")
        return name
    
    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("* Mensagem muito curta (mínimo 10 caracteres)")
        return message
    
    def clean_telephone(self):
        phone = self.cleaned_data["telephone"].strip()

        if not phone:
            return phone
        
        digits = re.sub(r"\D", "", phone)
        if len(digits) not in (10, 11):
            raise forms.ValidationError("* Celular inválido. Use DDD + número")
        return digits