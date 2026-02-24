from fastapi import FastAPI
from rotas import ibge,eleitores,comex
from fastapi.responses import RedirectResponse

app = FastAPI(title="EcoData-GRU API",
              description="""API para disponibilização de dados econômicos de Guarulhos, para suporte a tomada de decisão.
                            \n\n\nAlterar visualização:
                            - [Página de testes (Swagger UI)](/docs)
                            - [Página de leitura (ReDoc)](/redoc)
                          """,
              version="1.0.0",
              contact={"name": "Ulisses Calado",
                       "url": "https://github.com/ucalado/",
                       "email": "ulisses.scalado@gmail.com"})

app.include_router(ibge.router)
app.include_router(eleitores.router)
app.include_router(comex.router)


# redirecionamento para página de docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
