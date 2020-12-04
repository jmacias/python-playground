# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# Web Scraping
# Activate env
# .env/bin/activate
# Install Beautiful Soup 4
# pip install BeautifulSoup4
# pip install requests

# %% Import

# %%
import requests
from bs4 import BeautifulSoup

HTML = '''
 <!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p class="cp">My first paragraph.</p>
<ul>
    <li>Juan</li>
    <li>Malu</li>
    <li>Diego</li>
    <li>Lupe</li>
    
</ul>

</body>
</html> 
'''

ssoup = BeautifulSoup(HTML, 'html.parser')
print(ssoup.find('h1').string)
print([e.string for e in ssoup.find_all('li')])
print(ssoup.find('p', {'class': 'cp'}).string)

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
ssoup = BeautifulSoup(page.content, 'html.parser')
print(ssoup)
