cp wificonnect.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable wificonnect
sudo systemctl start wificonnect
sudo systemctl status wificonnect
