

# importing os.path module 
import os
from bs4 import BeautifulSoup


def test_simple_html():
    root_path = os.path.dirname(__file__)#os.getcwd()
    f = open(os.path.join(root_path,"roots\\simple.html"),"r")
    html = f.read()

    soup = BeautifulSoup(html,features="lxml")
    res= []
    for b in soup.find_all("b"):
        print(b.string)
        res.append(b.string)

    assert res == ["item","item1","item2","item3","item4"]