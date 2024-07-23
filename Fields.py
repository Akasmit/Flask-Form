from bs4 import BeautifulSoup

# Sample HTML template
html_template = """
<html>
    <head>
        <title>Sample Template</title>
    </head>
    <body>
        <div class="keep">
            <p>This field should be kept</p>
        </div>
        <div class="discard">
            <p>This field should be discarded</p>
        </div>
        <div class="keep">
            <p>This field should also be kept</p>
        </div>
    </body>
</html>
"""

# Parse the HTML template
soup = BeautifulSoup(html_template, 'html.parser')

# Define a function to filter elements
def filter_elements(soup, classes_to_keep):
    for element in soup.find_all():
        if element.get('class') and not set(element['class']).intersection(classes_to_keep):
            element.decompose()

# Define the classes to keep
classes_to_keep = {'keep'}

# Filter the elements
filter_elements(soup, classes_to_keep)

# Print the filtered HTML
filtered_html = soup.prettify()
print(filtered_html)

