#!/sbin/sh

busybox mount /system
busybox mount /data

if [ -f /system/etc/init.qcom.modem_links.orig.sh ]; 
  then
    rm -rf /system/etc/init.qcom.modem_links.sh
    cp /system/etc/init.qcom.modem_links.orig.sh /system/etc/init.qcom.modem_links.sh
  else
    cp /system/etc/init.qcom.modem_links.sh /system/etc/init.qcom.modem_links.orig.sh
fi
