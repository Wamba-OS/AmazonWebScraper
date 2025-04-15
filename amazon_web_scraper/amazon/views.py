## Imports
import string
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import quote_plus
from .forms import SearchForm

## Extra functions
# Function for checking user input so we have test cases
def check_alphanumeric(string):
    for char in string:
        if not (char.isalnum() or char.isspace()):
            return False
    return True

# Function to check if there is at least one character
def check_for_word(string):
    for letter in string:
        if letter.isalpha():
            return True
    return False


## View functions
# View for the initial welcome page. Basically
# it just displays the view.
def welcome(request):
    return render(request, 'amazon_task1/welcome_page.html')





# View for the page getting the user's search. 
# Returns the search template
def get_search(request):
    form = SearchForm()
    return render(request, 'amazon_task1/search_page.html', {'form': form})


# Need to do error checking and eventually 
# filtering here. Go to the page displaying 
# the results after a valid search or the
# error page.
def display_results(request):


    # Get the search from user
    if request.method == 'POST':

        form = SearchForm(request.POST)

        # Validate form
        if form.is_valid():
            search = form.cleaned_data['search']

            # Error Checking
            if not check_for_word(search):
                form.add_error('search', 'Search must contain at least one letter')
                return render(request, 'amazon_task1/search_page.html', {'form': form})
            
            warning_enabled = not check_alphanumeric(search)


            # Formulate the search
            formatted_search = quote_plus(search)


            # Encode the URL
            url = f"https://www.amazon.com/s?k={formatted_search}"


            # Create context dictionary
            context = {
                'search': search,
                'URL': url,
            }
            
            # Only add warning message if special characters are present
            if warning_enabled:
                context['warning_enabled'] = True
                context['special_chars_warning'] = "Your search contains special characters. Amazon may handle these differently than expected."
            
            # Display results with warning if needed
            return render(request, 'amazon_task1/results_page.html', context)

        
        # Else if form is invalid
        return render(request, 'amazon_task1/search_page.html', {'form': form})
    
    # Else if no search
    return redirect('search')
