# image_transmission_by_websocket

## Dockerfile described with opencv image for raspbian

## Build image:
>  sudo docker build -t <image_name>:<tag_name> <Dockerfile_directory>

## Run container directly:
>  sudo docker run --privileged -v /dev/video0:/dev/video0 --name=ed2ec -d -it hongsj1022/ai-go:ed2ec
