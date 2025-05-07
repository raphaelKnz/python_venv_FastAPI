from fastapi import FastAPI, Query 
import requests

app = FastAPI()

@app.get('/api/hello')
def bye_planet():
    return {'hello': 'world'}