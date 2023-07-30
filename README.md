# Simple-Extraction-GoogleSheets

Небольшое FastAPI приложение для извлечения данных из GoogleSheets

## Run ✈️

- Clone the project

```bash
  git clone https://github.com/mark47B/Simple-React-Chat.git
```

- Разворачиваем окружение Poetry

```bash
  poetry init
```

- Создаём виртуальное окружение

```bash
  poetry shell
```

- Устанавливаем зависимости

```bash
  poetry install --no-dev
```

- В папку 'secrets' добавляем credentials для GoogleAPI (стандартное название credentials.json, можно поменять в переменных окружения config/debug.env -> SERVICE_ACCOUNT_CREDENTIALS_PATH)

```bash
  poetry install
```

- Если под рукой Visual Studio Code, тогда можно открыть данный проект в нём, перейти во вкладку Run & Debug (Ctrl+Shift+D) и запустить uvicorn сервер, нажав на F5

- Если под рукой НЕТ Visual Studio Code, то следует выполнить следующую команду  

```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000
```

- Открываем http://0.0.0.0:8000/docs

```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000
```

<br/>