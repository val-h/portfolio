from django import forms

class ContactForm(forms.Form):
    # from_email = forms.EmailField(label='', widget=forms.TextInput(attrs={
    #     'placeholder': 'your.email@mail.com',
    #     'class': 'form-title',
    #     'cols': 40,
    # }))
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'class': 'form-title',
        'cols': 40,
    }))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': 'Your message',
        'class': 'form-text',
        'cols': 80,
    }))
    