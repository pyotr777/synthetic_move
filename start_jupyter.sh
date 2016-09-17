#!/bin/bash
# Start Jupyter notebook in docker mounting current folder with ipynb file.

echo "Starting Jupyter in Docker mounting current folder inside container."
echo "It will be available at http://localhost:8888 address."

MOUNT_DIR=/notebooks
IMAGE_REPO=tensorflow/tensorflow
if [[ $1 ]]; then
	IMAGE_TAG=":$1"
fi
IMAGE=$IMAGE_REPO$IMAGE_TAG
NAME=synt_tensor

docker run -d -p 8888:8888 --name $NAME -v $(pwd):$MOUNT_DIR $IMAGE
sleep 5
open http://localhost:8888
