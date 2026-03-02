from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from limiter_config import limiter
from rotas import caged, eleitores, comex, cnes

app = FastAPI(title="EcoData-GRU API",
              description="""
API para disponibilização de dados econômicos de Guarulhos, para suporte a tomada de decisão.
            
### Objetivo
Consolidar informações diversas, de várias áreas, secretarias, departamentos e orgãos municipais,
em um repositório único. Esse ecossistema permite:
* **Tratamento e análise:** Padronização de dados brutos de fontes distintas.
* **Agilidade:**Otimização do processo de produção de relatórios para gestão pública.
* **Transparência:** Facilitação do acesso a indicadores chave (KPIs) da cidade.

### Documentação alternativa
* [Página de testes (Swagger UI)](/docs)
* [Página de leitura (ReDoc)](/redoc)
""",
              version="1.0.0",
              contact={"name": "Ulisses Calado",
                       "url": "https://github.com/ucalado/",
                       "email": "ulisses.scalado@gmail.com"})

setattr(app.state, "limiter", limiter)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(ibge.router)
app.include_router(eleitores.router)
app.include_router(comex.router)
app.include_router(cnes.router)


# redirecionamento para página de docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
