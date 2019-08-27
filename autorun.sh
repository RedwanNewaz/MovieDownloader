#! /bin/bash

REMOTE_SRC="/usr/src/app"
REMOTE_DOWNLOAD="/Downloads"
REMOTE_LOG="/log"

LOCAL_SRC="/storage/RedSanSuz/product"
LOCAL_DOWNLOAD="/var/media/SANDY"
LOCAL_LOG="/var/media/SANDY"

IMG_NAME="movieserver"
function MovieDownloadServer()
{

echo "[MovieDownloadServer ]: Starting ........."
    docker run -d \
        -v $LOCAL_SRC:$REMOTE_SRC \
        -v $LOCAL_DOWNLOAD:$REMOTE_DOWNLOAD \
        -v $LOCAL_LOG:$REMOTE_LOG \
        -p 80:80 \
        $IMG_NAME

echo "[MovieDownloadServer ]: Started"
}


CONFIG="/storage/RedSanSuz/GoogleHomeKodiConfig"
function GoogleHomeKodi()
{
  
echo "[GoogleHomeKodi ]: Starting ........."
    docker run \
   -d \
   --publish 8099:8099 \
   --restart always \
   -v $CONFIG:/config \
   --name googlehomekodi \
   omertu/googlehomekodi

echo "[GoogleHomeKodi ]: Started"
}

MovieDownloadServer
GoogleHomeKodi


 