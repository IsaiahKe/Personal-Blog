import urllib.request,json  
from app.models import Quote



def get_quote():
    path="http://quotes.stormconsultancy.co.uk/random.json"
    with urllib.request.urlopen(path) as url:
        url_data=url.read()
        formated_data=json.loads(url_data)
        #tie url data to quote object properties
        id=formated_data.get('id')
        quote=formated_data.get('quote')
        author=formated_data.get('author')
        link=formated_data.get('permalink')
            
        newquote=Quote(author,id,quote,link)
        print(newquote.quote)
        #get quote 
        return newquote
