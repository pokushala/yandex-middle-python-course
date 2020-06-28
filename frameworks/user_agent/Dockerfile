FROM python:3.8-buster AS install

RUN python -m venv /opt/user_agent

ENV PATH="/opt/user_agent/bin:$PATH"

COPY ./requirements.txt .

RUN pip install  -r requirements.txt

RUN mkdir user_agent

COPY user_agent ./user_agent/user_agent
COPY setup.py ./user_agent

RUN pip install ./user_agent

FROM python:3.8-buster AS build
COPY --from=install /opt/user_agent /opt/user_agent

ENV PATH="/opt/user_agent/bin:$PATH"

COPY wsgi.py .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:wsgi"]

EXPOSE 8000


