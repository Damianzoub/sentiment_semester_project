import re

#clean text from html tags
def clean_html_tags(text):
    if not isinstance(text,str):
        return " "
    
    text = re.sub(r'<br\s*/?>',' ',text)
    text = re.sub(r'<.*?>',' ',text)
    text = re.sub(r'\s+',' ',text).lower().strip()
    return text