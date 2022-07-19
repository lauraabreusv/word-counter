from django import forms

class TextForm(forms.Form):
    text = forms.CharField(
        label='',
        widget= forms.Textarea(attrs={'required': 'True', 'width': '100%', 'height':'100px'}),
        required=False,
        
    )