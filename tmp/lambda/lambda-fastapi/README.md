# lambda-fastapi

API FastAPI executando no AWS Lambda via Mangum.

## Rodar localmente
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```
Docs: http://127.0.0.1:8000/docs

## Gerar o pacote
```powershell
.\build.ps1
```

## Deploy pelo Console AWS
1. Lambda → Create function → Python 3.12, x86_64.
2. Code → Upload from → .zip file → `lambda.zip`.
3. Runtime settings → Handler: `app.main.handler`.
4. Configuration → General: 512 MB, timeout 15 s.
5. Configuration → Environment variables: `AMBIENTE=aws` (opcional).
6. Configuration → Function URL → Create (auth `NONE` apenas para a aula).
7. Abrir `<function-url>/docs`.

Ao terminar, exclua a Function URL, a função, a role e o log group.
