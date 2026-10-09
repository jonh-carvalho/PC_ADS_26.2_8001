$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Remove-Item -Recurse -Force package, lambda.zip -ErrorAction SilentlyContinue

pip install -r requirements.txt `
    --platform manylinux2014_x86_64 --target package `
    --implementation cp --python-version 3.12 --only-binary=:all:
if ($LASTEXITCODE -ne 0) { throw "Falha no pip install" }

Copy-Item -Recurse app package\app
Get-ChildItem package -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
Compress-Archive -Path package\* -DestinationPath lambda.zip -Force

"{0:N1} MB -> lambda.zip" -f ((Get-Item lambda.zip).Length / 1MB)
