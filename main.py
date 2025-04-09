import markdown
##convert md to html 

def md_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html
if __name__ == "__main__":
    markdown_text = """
# Hello World
This is a sample markdown text.
## Features
- Feature 1
- Feature 2
## Code
"""
html_out = md_to_html(markdown_text)
print(html_out)