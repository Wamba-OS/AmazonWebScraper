from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a search term',
            'class': 'search-input'
        })
    )