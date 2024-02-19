sudo systemctl disable wificonnect
sudo systemctl stop wificonnect
rm  /etc/systemd/system/wificonnect.service
sudo systemctl daemon-reload

