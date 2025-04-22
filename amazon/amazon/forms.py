from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(
        label="Search", 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter a search term'})
    )
    min_price = forms.IntegerField(
        label="Min Price (USD)", 
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '0'})
    )
    max_price = forms.IntegerField(
        label="Max Price (USD)", 
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '1000'})
    )
    company = forms.CharField(
        label="Brand/Company", 
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Apple, Samsung, Dell'})    
    )
    category = forms.ChoiceField(
        label="Category",
        choices=[
             ('', 'All Categories'),
            ('electronics', 'Electronics'),
            ('books', 'Books'),
            ('fashion', 'Fashion'),
            ('toys', 'Toys'),
            ('home', 'Home'),
            ('kitchen', 'Kitchen'),
            ('beauty', 'Beauty'),
            ('sports', 'Sports & Outdoors'),
            ('automotive', 'Automotive'),
            ('health', 'Health & Household'),
            ('grocery', 'Grocery'),
            ('tools', 'Tools & Home Improvement'),
            ('garden', 'Garden & Outdoor'),
            ('baby', 'Baby'),
            ('pets', 'Pet Supplies'),
            ('office', 'Office Products'),
            ('music', 'CDs & Vinyl'),
            ('movies', 'Movies & TV'),
            ('games', 'Video Games')
        ],
        required=False
    )
