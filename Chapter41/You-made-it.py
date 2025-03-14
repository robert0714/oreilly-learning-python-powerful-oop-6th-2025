"""
Generate a simple class completion certificate: printed to
the console, and saved in auto-opened text and HTML files.
Run from a console, and print saved output files if desired.
Works on all PCs, but may require manual opens on smartphones.
"""
import time, sys, html, os

maxline = 60                               # Text separator lines
browser = True                             # Display in a browser?
saveto  = 'Certificate'                    # Output filenames prefix

# Template values
SEPT = '*' * maxline
DATE = time.strftime('%A, %b %d, %Y, %I:%M %p')
NAME = input('Please enter your name: ').strip() or 'An unknown reader'
BOOK = 'Learning Python, 6th Edition'
SITE = 'https://learning-python.com'       # For icon, image, link

# F-string templates work for preset in-code references
texttext = f"""
{SEPT}

⭐️ Official Certificate ⭐️

Date: {DATE}

This certifies that:

\t{NAME}

Has survived the massive tome:

\t{BOOK}

And is now entitled to all privileges thereof, including
the right to proceed on to learning how to develop websites,
desktop GUIs, scientific models, smartphone apps, and 
anything else that the future of computing may hold. 

--Your humble 🐍 instructor

(Note: void where obtained by skipping ahead.)

{SEPT}
"""

# Interact, setup
for c in 'Congratulations!'.upper() + '👏' * 3:
    print(c, end=' ')
    sys.stdout.flush()    # Else some shells wait for \n
    time.sleep(0.25)      # Reveal message slowly for fun
print(); time.sleep(3)

# Make text-file version
textto = saveto + '.txt'
fileto = open(textto, 'w', encoding='utf8')
print(texttext, file=fileto)
fileto.close()

# Start HTML: replace text markers with tags
htmltext = texttext.replace(SEPT,   '<div class=cert>', 1)
htmltext = htmltext.replace(SEPT,   '</div>')
htmltext = htmltext.replace('⭐️ ', '<h1 align=center>⭐️&nbsp;', 1)
htmltext = htmltext.replace(' ⭐️', '&nbsp;⭐️</h1>')

# Line-by-line mods
linemods = []
for line in htmltext.split('\n'):
    if line == '':
        line = '<p>'
    elif line[:1] == '\t':
        line = f"<i>{'&nbsp;' * 4}{html.escape(line[1:])}</i>"   # 3.6+
    linemods.append(line)
htmltext = '\n'.join(linemods)
     
# Ignorable HTML bits (mind the {{ and }} escapes)
preamble = f'''<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/x-icon" href="{SITE}/favicon.ico">
<style> 
body  {{font-family: Arial, Helvetica, sans-serif;}} 
.cert {{background-color: cornsilk; padding: 16px; border: medium solid black;}}
</style>
<title>LP6E Completion Certificate</title>
</head>
'''

image, page = 'lp6e-large.jpg', 'about-lp.html'
footer = f'''
<table><tr>
<td><a href="{SITE}/{page}"><img src="{SITE}/{image}" hspace=10 height=50></a>
<td><a href="{SITE}/{page}" align=center><i>Book support site</i></a>
</tr></table>
'''

# Put it all together
htmltext = f'{preamble}<body bgcolor="#eee">{htmltext}{footer}</body></html>'

# Make HTML-file version
htmlto = saveto + '.html'
fileto = open(htmlto, 'w', encoding='utf8')
print(htmltext, file=fileto)
fileto.close()

# Display text results in console
print(f'[File: {textto}]', end='')
print('\n' * 2, open(textto, encoding='utf8').read())

# Open docs (may also fail silently)
if browser:
    try:
        import webbrowser
        for doc in (textto, htmlto):
            webbrowser.open('file://' + os.path.abspath(doc))
    except Exception:
        print('Unable to auto-open docs: open manually.')

input('[Press Enter to close]')    # Keep window open if clicked

