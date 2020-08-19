# UniChess

- Criar ambiente virtual

```bash
    python3 -m venv .venv
    source .venv/bin/activate
```

- SQLite3

```bash
    sudo apt install sqlite3
```

- Instalar

```bash
    make install
```

- Executar

```bash
    make run
```

- Rodar linters

```bash
    make format
```

- Rodar testes

```bash
    make test
```

- Limpar e reinicializar

```bash
    make clean
```

- Implementar logging

```python
    from flask import current_app

    # Com DEBUG_TB_ENABLED em ext/config
    current_app.logger.debug("message")
```

