FROM python:3.11

RUN pip install poetry

COPY poetry.lock pyproject.toml /
COPY ./discord_bot ./discord_bot
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

CMD python discord_bot/bot.py