import markdown

somemd = """
# Mayil

This is is so <<<<< ??? >>>>> 
"""

html = markdown.markdown(somemd, tab_length=12)
print("|", html, "|")
print("---------------------------------")