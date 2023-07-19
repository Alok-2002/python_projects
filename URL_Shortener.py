from pyshorteners import *
from pyperclip import *


url = input("Enter The URL That You Want To Make Short: ")


def shortenurl(url):
    s = Shortener()
    print(s.tinyurl.short(url))
    
    
shortenurl(url)
