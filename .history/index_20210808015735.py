from fastapi import FastAPI
from googlesearch import search

app = FastAPI()

app.get('/pesq/')
def pesq(q:str,n:int=10,lg:str='en'):
    return search(term=q,num_results=n,lang=lg)