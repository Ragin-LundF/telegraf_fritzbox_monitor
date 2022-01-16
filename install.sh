#!/bin/bash

DEST_DIR=/opt/telegraf_fritzbox

# copy config to telegraf
cp telegraf_fritzbox.conf /etc/telegraf/telegraf.d/

# create directory
mkdir -p ${DEST_DIR}
cp telegraf_fritzbox.py ${DEST_DIR}/
cp -fR models ${DEST_DIR}/
cp -fR modules ${DEST_DIR}/
