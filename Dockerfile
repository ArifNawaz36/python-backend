FROM python:3.10

RUN pip install --upgrade pip

ENV POETRY_HOME=/poetry

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/poetry/bin:${PATH}"

RUN poetry --version

WORKDIR /var/task

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install

COPY ./src .

CMD [ "uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80" ]