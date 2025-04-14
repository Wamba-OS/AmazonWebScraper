## Imports
from django.shortcuts import render

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


