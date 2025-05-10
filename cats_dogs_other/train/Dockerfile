FROM python:3.11-slim

# Variables passées au moment du build
ARG MLFLOW_S3_ENDPOINT_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# Variables d’environnement dans le conteneur
ENV MLFLOW_S3_ENDPOINT_URL=${MLFLOW_S3_ENDPOINT_URL}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

# Copie des fichiers du projet
COPY cats_dogs_other/train/train.py ./cats_dogs_other/train/train.py
COPY cats_dogs_other/train/MLproject ./cats_dogs_other/train/MLproject
COPY cats_dogs_other/train/kubernetes_config.json ./cats_dogs_other/train/kubernetes_config.json
COPY cats_dogs_other/train/kubernetes_job_template.yaml ./cats_dogs_other/train/kubernetes_job_template.yaml
COPY cats_dogs_other/requirements.txt ./cats_dogs_other/requirements.txt
COPY cats_dogs_other/train/packages/kto_keras_inference-0.0.1-py3-none-any.whl ./cats_dogs_other/train/packages/kto_keras_inference-0.0.1-py3-none-any.whl
COPY packages ./packages
COPY init_packages.sh ./init_packages.sh

# Permissions et installation
RUN chmod -R 777 ./cats_dogs_other
RUN chmod +x ./init_packages.sh
RUN ./init_packages.sh
RUN pip install -r ./cats_dogs_other/requirements.txt
