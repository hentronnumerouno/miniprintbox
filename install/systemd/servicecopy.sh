cp miniprint.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable miniprint.service
sudo systemctl start miniprint.service
sudo systemctl status miniprint.service
