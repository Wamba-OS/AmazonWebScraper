## Imports
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import quote_plus



## View functions
# View for the initial welcome page. Basically
# it just displays the view.
def welcome(request):
    return render(request, 'amazon_task1/welcome_template.html')





# View for the page getting the user's search. 
# Returns the search template
def get_search(request):
    return render(request, 'amazon_task1/search_page.html')


# Need to do error checking and eventually 
# filtering here. Go to the page displaying 
# the results after a valid search or the
# error page.
def display_results(request):

    # Get the search from user
    if request.method == 'POST':
        search = request.POST.get('search_query,' '')

        # Formulate the search
        formatted_search = quote_plus(search)


        # Error Checking


        # Encode the URL
        url = f"https://www.amazon.com/s?k={formatted_search}"

        # Display results
        return render(request, 'amazon_task1/results_page.html', {
            'search': search,
            'URL': url
        })
    
    # Else
    return redirect('amazon_task1/search_page.html')
