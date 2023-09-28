from bs4 import BeautifulSoup

# Example HTML content
html = """
<div class="rt-tr-group">
    <div class="rt-tr">
        <div class="rt-td winrate">
            <span>
                <b>Child 1</b>
                <b>Child 2</b>
            </span>
        </div>
    </div>
</div>
"""

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the elements matching the selector
elements = soup.select('.rt-tr-group .rt-tr .rt-td.winrate span b')

# Loop through the elements and print their text content
for element in elements:
    print(element.text)
