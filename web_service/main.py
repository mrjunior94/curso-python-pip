import uvicorn
from fastapi import FastAPI 
from fastapi.responses import HTMLResponse  

app = FastAPI ()

@app.get('/')
def get_list():
    return [1]

@app.get('/choneta', response_class=HTMLResponse)
def get_list():
    return '''
    <h1>Hello, aqui viendo como enviarte mensajes</h1>
    '''

def run():
    uvicorn.run("main:app", reload=True)

if __name__ == "__main__": 
    run()  