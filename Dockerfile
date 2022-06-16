FROM python:3.8.13-slim-buster@sha256:00603941e626c09b20cba7d4cce52e34c683c47ca332f447c0d55aa1179209ce

USER root
RUN groupadd -r vasyandre && useradd -r -g vasyandre vasyandre && python -m pip install Django==4.0.5
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN chown -R vasyandre:vasyandre /app && chmod +x entrypoint-django.sh
USER vasyandre
ENTRYPOINT [ "./entrypoint-django.sh" ]

