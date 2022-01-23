#!/bin/bash

DEST_DIR=/opt/telegraf_fritzbox

# copy config to telegraf, but don't overwrite it
if [[ ! -e /etc/telegraf/telegraf.d/telegraf_fritzbox.conf ]]; then
  cp telegraf_fritzbox.conf /etc/telegraf/telegraf.d/
fi

# create directory
mkdir -p ${DEST_DIR}
cp telegraf_fritzbox.py ${DEST_DIR}/
cp config.yaml ${DEST_DIR}/
cp -fR models ${DEST_DIR}/
cp -fR modules ${DEST_DIR}/
