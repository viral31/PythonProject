FROM public.ecr.aws/lambda/python:3.11

# Copy requirements and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

# Copy source code
COPY ./app ${LAMBDA_TASK_ROOT}/app

# Set the CMD to the Lambda handler
CMD ["app.lambda_handler.handler"]
