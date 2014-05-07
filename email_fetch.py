import sys
import imaplib
import getpass
import email
import email.header
import datetime
from bs4 import BeautifulSoup 
import re
from lxml import etree, html
from HTMLParser import HTMLParser
from lxml.html import fromstring, tostring
from lxml.html.clean import Cleaner, clean_html
from itertools import chain


EMAIL_ACCOUNT = "sample@gmail.com"
EMAIL_FOLDER = "INBOX"
 

def stringify_children(node):
    parts = ([node.text] +
            list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) +
            [node.tail])
    return ''.join(filter(None, parts))
 
def process_mailbox(M):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """
 
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print "No messages found!"
        return
    for num in data[0].split(): 
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return
 
        msg = email.message_from_string(data[0][1])
        
        if msg.is_multipart():
            html = None
            print "Checking for html or text"
            for part in msg.get_payload():
                if part.get_content_charset() is None:
                    charset = chardet.detect(srt(part))['encoding']
                else:
                    charset = part.get_content_charset()
                if part.get_content_type() == 'text/plain':
                    text = unicode(part.get_payload(decode=True),str(charset),"ignore").encode('utf8','replace')
                    f = open('email.txt', 'w')
                    f.write(text)
                    f.close
                if part.get_content_type() == 'text/html':
                    html = unicode(part.get_payload(decode=True),str(charset),"ignore").encode('utf8','replace')
                    f = open('email.html','w')
                    f.write(html)
                    f.close
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()

                if not os.path.isfile(filename) :
                    fp = open(filename, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    return 0

            if html is None:
                return text.strip()
            else:
                return html.strip()
 

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



    

def parse_html():
    soup = BeautifulSoup(open("email.html"))
    VALID_TAGS = ['iframe', 'video', 'o>', 'li', 'sub', 'sup', 'source', 'br', 'h3', 'h4', 'h6', 'hr', 'q', 'mark','wbr', 'audio','strong', 'em', 'p','ul', 'li', 'br', 'blockquote', 'pre', 'del', 'h3', 'body', 'header', 'html', 'title', 'div', 'img', 'a']

    for tag in soup.findAll(True):
        if tag.name == 'i':
            tag.name = 'em'
        elif tag.name == 'cite':
            tag.name = 'em'
        elif tag.name == 'b':
            tag.name = 'strong'
        elif tag.name == 'kdb':
            tag.name = 'strong'
        elif tag.name == 'var':
            tag.name = 'strong'
        elif tag.name == 'aside':
            tag.name = 'blackquote'
        elif tag.name == 'code':
            tag.name = 'pre'
        elif tag.name == 'samp':
            tag.name = 'pre'
        elif tag.name == 's':
            tag.name = 'del'
        elif tag.name == 'h1':
            tag.name = 'h3'
        elif tag.name == 'h2':
            tag.name = 'h3'
        elif tag.text == "" or None:
            tag.extract()
    
    pretty_soup = soup.prettify().encode('utf8')
    docstring = str(pretty_soup)
    
    tree = etree.fromstring(docstring)
    walkAll = tree.iter()
    count = 0
    for elt in walkAll:
        if count <= 50:
            child = stringify_children(elt)
            childtext = strip_tags(child)
            childstring = childtext.replace(" ", "")
            for i in childstring:
                if count <=50:
                    count = count + len(i)
                elif count > 50:
                    pass
        elif count > 50:
            elt.text = ""
              
    
    etroot = tree.getroottree()
    results = etree.tostring(etroot)
    htmldoc = open("email.html", "r+")
    htmldoc.write(results)
    
                
    
                                    

M = imaplib.IMAP4_SSL('imap.gmail.com')
 
try:
    rv, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
    print "LOGIN FAILED!!! "
    sys.exit(1)
 
print rv, data
 
rv, mailboxes = M.list()
if rv == 'OK':
    print "Mailboxes:"
    print mailboxes
 
rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    print "Processing mailbox...\n"
    process_mailbox(M)
    M.close()
    parse_html()
else:
    print "ERROR: Unable to open mailbox ", rv
 
M.logout()
