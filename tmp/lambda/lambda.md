# Roteiro: AWS Lambda + FastAPI com deploy pelo Console AWS

**Duração sugerida:** 2h | **Nível:** introdutório | **Pré-requisitos:** Python 3.12, conta AWS (Free Tier), noções de HTTP/REST

## Objetivos
- Explicar o modelo serverless e quando usar AWS Lambda.
- Construir uma API REST com FastAPI.
- Adaptá-la ao Lambda com o Mangum (adaptador ASGI).
- Empacotar e publicar pelo Console AWS, expondo via Function URL / API Gateway.
- Monitorar com CloudWatch; conhecer custos e limites.

## Cronograma

| Tempo | Bloco | Formato |
|---|---|---|
| 0:00–0:15 | 1. Conceitos: serverless e Lambda | Exposição |
| 0:15–0:25 | 2. FastAPI em 10 minutos | Exposição + demo |
| 0:25–0:50 | 3. Desenvolvimento local | Prática |
| 0:50–1:05 | 4. Empacotamento (.zip) | Prática |
| 1:05–1:35 | 5. Deploy pelo Console AWS | Prática guiada |
| 1:35–1:50 | 6. Testes, logs e monitoramento | Prática |
| 1:50–2:00 | 7. Custos, limites e encerramento | Discussão |

---

## 1. Conceitos (15 min)
- **Serverless:** sem gerenciar servidores; paga-se por invocação e tempo de execução.
- **Lambda:** função disparada por eventos (HTTP, S3, SQS, agendamento...).
- Termos: *handler*, *runtime*, *cold start*, memória/timeout, role IAM, layers.
- Limites: timeout máx. 15 min; zip até 50 MB (250 MB descompactado).
- Fluxo: `Cliente → Function URL (ou API Gateway) → Lambda → FastAPI (via Mangum)`.

## 2. FastAPI em 10 minutos
- Framework ASGI, Pydantic, documentação automática em `/docs`.
- O Lambda entrega um *evento JSON*; o **Mangum** o converte em requisição ASGI.

## 3. Desenvolvimento local (25 min)

```
lambda-fastapi/
├── app/
│   └── main.py
└── requirements.txt
```

`requirements.txt`
```
fastapi
mangum
```

`app/main.py`
```python
from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI(title="API Lambda")

class Item(BaseModel):
    nome: str
    preco: float

itens: list[Item] = []  # memória volátil: não persiste entre execuções

@app.get("/")
def raiz():
    return {"mensagem": "FastAPI rodando no AWS Lambda"}

@app.get("/itens")
def listar():
    return itens

@app.post("/itens", status_code=201)
def criar(item: Item):
    itens.append(item)
    return item

handler = Mangum(app)
```

Execução local:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi mangum "uvicorn[standard]"
uvicorn app.main:app --reload
```
Abrir `http://127.0.0.1:8000/docs`.

> **Discussão:** por que a lista em memória não serve no Lambda? (instâncias efêmeras → DynamoDB como evolução).

## 4. Empacotamento (15 min)

Dependências compiladas (ex.: `pydantic-core`) devem ser binários Linux. No Windows:

```powershell
pip install -r requirements.txt `
  --platform manylinux2014_x86_64 --target package `
  --implementation cp --python-version 3.12 --only-binary=:all:
Copy-Item -Recurse app package\app
Compress-Archive -Path package\* -DestinationPath lambda.zip -Force
```
Conferir que `app/` e as bibliotecas ficam na **raiz** do zip.

## 5. Deploy pelo Console AWS (30 min)

1. Console AWS → escolher região (ex.: `sa-east-1`) → serviço **Lambda**.
2. **Create function** → *Author from scratch*:
   - Nome `fastapi-demo`, Runtime **Python 3.12**, Arquitetura **x86_64** (igual ao pacote).
   - Role básica do Lambda (logs no CloudWatch).
3. Aba **Code** → *Upload from* → **.zip file** → `lambda.zip` → *Save*.
   - Zip grande: enviar a um bucket **S3** e informar o link.
4. **Runtime settings → Edit**: Handler = `app.main.handler`.
5. **Configuration → General configuration**: 512 MB, timeout 15 s.
6. **Configuration → Function URL → Create function URL**:
   - Auth `NONE` (só na aula; em produção usar `AWS_IAM` ou API Gateway + autorizador).
7. *(Extensão)* **API Gateway → HTTP API**, integração Lambda, rota `ANY /{proxy+}`.
8. Acessar `<function-url>/` e `<function-url>/docs`.

> Com API Gateway e *stage*, usar `Mangum(app, api_gateway_base_path="/stage")` e `FastAPI(root_path="/stage")`.

## 6. Testes, logs e monitoramento (15 min)
- Aba **Test**: evento de teste (modelo *apigw-http-api*) e leitura do resultado.
- curl:
  ```powershell
  curl <function-url>/itens
  curl -X POST <function-url>/itens -H "Content-Type: application/json" -d '{"nome":"caneta","preco":3.5}'
  ```
- **Monitor → CloudWatch logs**: linhas `START/END/REPORT` (duração, memória, *Init Duration* = cold start).
- Experimento: comparar cold start × warm.

## 7. Custos, limites e encerramento (10 min)
- Free Tier: 1 M requisições e 400 mil GB‑s/mês.
- Boas práticas: menor privilégio no IAM, variáveis de ambiente, layers, evitar URL pública sem auth.
- **Limpeza:** excluir Function URL, função, role, log group e API Gateway.

## Atividade sugerida
1. Adicionar `PUT /itens/{id}` e `DELETE /itens/{id}`.
2. Expor em `/info` uma variável de ambiente (`AMBIENTE`) definida no console.
3. Entregar: código no GitHub, print dos logs do CloudWatch e URL (desativada após correção).

## Próximos passos
DynamoDB, AWS SAM/CLI, CI/CD com GitHub Actions, imagem de container no Lambda, autenticação com Cognito.

## Referências
- https://docs.aws.amazon.com/lambda/
- https://fastapi.tiangolo.com
- https://mangum.fastapiexpert.com
