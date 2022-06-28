# Instruções

## 1. Instalação
```bash
make install
```
## 2. Iniciar aplicação
```bash
make run
```

# Cobertura
Para rodar a ferramenta de cobertura localmente, primeiro é necessário instalar o coverage:

    pip intall coverage

Depois, na pasta `busondi/` rode o seguinte comando, para que a cobertura seja calculada:

    coverage run --source=backend --omit=backend/tests/* -m unittest discover backend/tests/unity/

Então, gere o relatório no formato desejado. 

    coverage html

No caso do formato html, o relatório será gerado na pasta `busondi/htmlcov/`. Basta abrir o arquivo `htmlcov\index.html` e poderá ver a cobertura dos arquivos, até o nível de linha.

## Codecov

Verifique a cobertura do backend pelo [Codecov](https://app.codecov.io/gh/arthurrlisboa/busondi).