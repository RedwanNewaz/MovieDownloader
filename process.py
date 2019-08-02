#!/Python27/python 

import json
from manager import ProgramManager
mobileView='<meta name="viewport" content="width=device-width, initial-scale=1.0">'
progress=' <p id="p1"><label for="file">Download in progress:</label> </p> <progress id="file" max="100" value="30"> 30% </progress><br>'
print "Content-type: text/html"
print
print "<html><head>"
print ""
print mobileView
print "</head><body>"
print progress
program = ProgramManager()
program.execute()
print "</body></html>"