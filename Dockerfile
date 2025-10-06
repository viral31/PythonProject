FROM public.ecr.aws/lambda/python:3.11

# Copy Lambda Web Adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter

# Set environment variables for Lambda Web Adapter
ENV AWS_LWA_INVOKE_MODE=RESPONSE_STREAM
ENV AWS_LWA_PORT=8000

# Copy requirements and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

# Copy source code
COPY ./app ${LAMBDA_TASK_ROOT}/app

# Create startup script
RUN echo '#!/bin/bash\nuvicorn app.main:app --host 0.0.0.0 --port 8000' > /start.sh && chmod +x /start.sh

# Set the CMD
CMD ["/start.sh"]
