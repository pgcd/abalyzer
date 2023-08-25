FROM public.ecr.aws/lambda/python:3.11
LABEL authors="pgcd"

COPY requirements.txt ${LAMBDA_TASK_ROOT}

COPY abalyzer.py ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

CMD [ "abalyzer.lambda_handler" ]
