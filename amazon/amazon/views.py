## Imports
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import quote_plus
from .forms import SearchForm



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
    # Debug the POST data
    print("Raw POST data:", dict(request.POST))
    
    if request.method == 'POST':
        # Get values directly from POST data
        search = request.POST.get('search', '')
        min_price_str = request.POST.get('min_price', '')
        max_price_str = request.POST.get('max_price', '')
        category = request.POST.get('category', '')
        company = request.POST.get('company', '')
        
        # Convert price strings to integers if they're not empty
        min_price = None
        if min_price_str and min_price_str.strip():
            try:
                min_price = int(min_price_str)
            except ValueError:
                pass
                
        max_price = None
        if max_price_str and max_price_str.strip():
            try:
                max_price = int(max_price_str)
            except ValueError:
                pass
        
        # Debug values
        print(f"Parsed values: search={search}, min_price={min_price}, max_price={max_price}, category={category}, company={company}")
        
        # Start with the base search
        formatted_search = quote_plus(search)
        url = f"https://www.amazon.com/s?k={formatted_search}"
        
        # Build filter parameters
        filter_parts = []
        
        # Add price filter
        if min_price is not None or max_price is not None:
            min_cents = int(min_price or 0) * 100
            max_cents = int(max_price or 1000000) * 100
            filter_parts.append(f"p_36%3A{min_cents}-{max_cents}")
        
        # Add category filter
        if category:
            category_node_ids = {
                'electronics': 'n%3A172282',
                'books': 'n%3A283155',
                'fashion': 'n%3A7141123011',
                'toys': 'n%3A165793011',
                'home': 'n%3A1055398',
                'kitchen': 'n%3A284507',
                'beauty': 'n%3A3760911',
                'sports': 'n%3A3375251',
                'automotive': 'n%3A15684181',
                'health': 'n%3A3760901',
                'grocery': 'n%3A16310101',
                'tools': 'n%3A228013',
                'garden': 'n%3A2972638011',
                'baby': 'n%3A165796011',
                'pets': 'n%3A2619533011',
                'office': 'n%3A1064954',
                'music': 'n%3A5174',
                'movies': 'n%3A2625373011',
                'games': 'n%3A468642'
            }
            if category in category_node_ids:
                filter_parts.append(category_node_ids[category])
            # Add company/brand filter
        if company:
            # URL encode the company name and add it to the filter parts
            encoded_company = quote_plus(company)
            filter_parts.append(f"p_89%3A{encoded_company}")
        
        # Append filters to URL if any exist
        if filter_parts:
            url += "&rh=" + ",".join(filter_parts)
        
        # Debug final URL
        print("Final URL:", url)
        
        return render(request, 'amazon_task1/results_page.html', {
            'search': search,
            'min_price': min_price,
            'max_price': max_price,
            'category': category,
            'company': company,
            'URL': url
        })
    
    # GET request
    return redirect('get_search')