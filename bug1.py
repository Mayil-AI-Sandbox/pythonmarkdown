import markdown

somemd = """
Our package should be able to handle HTML in markdown files. Here is an example markdown file with HTML:
'''
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
'''
But there is a bug

"""

html = markdown.markdown(somemd)
print(html)
print("---------------------------------")


"""
Returned output:
<p>Our package should be able to handle HTML in markdown files. Here is an example markdown file with HTML:
'''</p>
<p>wzxhzdk:0</p>
<p>wzxhzdk:1</p>
<p>'''
But there is a bug</p>
("---------------------------------")

Expected output:
<p>Our package should be able to handle HTML in markdown files. Here is an example markdown file with HTML:
'''</p>
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
<p>'''
But there is a bug</p>
"""