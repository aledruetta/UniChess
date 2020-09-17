# UniChess

### Estado Atual do projeto

[<img src="art/youtube.png" width="50%">](https://youtu.be/bj4vwHOVqo8)

### Instalar e executar

- Criar ambiente virtual

```bash
    python3 -m venv .venv
    source .venv/bin/activate
```

- SQLite3

```bash
    sudo apt install sqlite3
    sudo apt install shellcheck
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
    make lint
```

- Rodar testes

```bash
    make test
```

- Limpar e reinicializar

```bash
    make clean
```

- Database

```bash
    # Inicial migration
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

    # After git clone
    make initdb
    flask db migrate -m "Comment migration"
    flask db upgrade

    # Admin commands
    flask createadb
    flask createadmin
    flask createuser
    flask listusers
```
