import markdown

somemd = """
# Mayil

This is is so <<<<< ??? >>>>> 
"""

html = markdown.markdown(somemd, tab_length=12)
print("|", html, "|")
print("---------------------------------")


''''
Expected output:
| <h1>Mayil</h1>
<p>This is is so &lt;&lt;&lt;&lt;&lt; ??? &gt;&gt;&gt;&gt;&gt; </p> |
---------------------------------

Returned output:
| <h1>Mayil</h1>
<p>This is is so &lt;&lt;&lt;&lt;&lt; ??? >>>>> </p> |
'''