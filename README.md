python-scripts
==============

Assorted Python Scripts 


email_fetch.py

    email_fetch.py logs into gmail and retrieves an email, parses it and saves the text to an email.txt file and the html to an email.html file,  then it opens the email.html file and does a DOM tree cleanup and sanitizing of any unsafe html tags, counts the text of each tag and once the    total text count reaches the count limit, the remaining tags are truncated to remove remaining text.
