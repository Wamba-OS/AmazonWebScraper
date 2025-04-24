# Description
This GitHub repository contains the work of group 5 (Nathanael Jense, Samuel Karlin, Nathan Schluessler) in Dr. Moin's CS 3300 Spring 2025 class at UCCS. We created a 3rd party online shopping site. It is currently set up to work with Amazon.com exclusively. The user can enter a search and apply filters all at once before receiving a link that directs them to the Amazon webpage that provides the results for their specific search. Currently, the website is run on a Django project hosted locally. 

# Instructions to Run the Server
1. Download GitHub repository or clone it from GitHub
git clone https://github.com/Wamba-OS/AmazonWebScraper

2. Set your active directory to wherever you installed the repository

3. Navigate to the Django project folder:
"cd AmazonWebScraper"

4. Install Django locally (or use a virtual environment):
"pip install -r requirements.txt"

5. Run command to launch site:
"python manage.py runserver"

After navigating to the website, you can follow the prompts
You will be given a URL to the website.
Clicking on the given link or typing out the URL in your browser will direct you to our website.

On the website you can type anything you would like to search for in the search bar and apply filters. Then press the "generate URL" button. This will navigate you to a page showing an Amazon URL to the search page on Amazon's official website displaying the results of your search. Finally, you can press "visit site" or click on the link directly to navigate to the given URL without having to type it into your browser.

# Next steps
In the future, we would like to host the website on a dedicated server either in the cloud or somewhere else to provide constant access to users. Additionally, we would like to partner with Amazon and obtain their API which would allow us to display the results of a user's search locally instead of simply redirecting them to Amazon.
