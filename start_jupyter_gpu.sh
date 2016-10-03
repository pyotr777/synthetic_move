#!/bin/bash
# Start Jupyter notebook in docker mounting current folder with ipynb file.

echo "Starting Jupyter in Docker mounting current folder inside container."
echo "It will be available at http://localhost:8888 address."

MOUNT_DIR=/notebooks
IMAGE_REPO=tensorflow/tensorflow:0.10.0-gpu
if [[ $1 ]]; then
	IMAGE_TAG=":$1"
fi
IMAGE=$IMAGE_REPO$IMAGE_TAG
NAME=pyotr777_synth_gpu #synt_tensor

nvidia-docker run -d -p 8888:8888 --name $NAME -v $(pwd):$MOUNT_DIR $IMAGE
sleep 5
open http://localhost:8888
