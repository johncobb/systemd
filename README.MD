<h2>systemd</h2>

Systemd is used to automatically start the ppp dialer services and dependent modules.

Important comands:
'''
systemctl enable service-name
systemctl disable service-name
systemctl start service-name
systemctl restart service-name
systemctl status service-name
'''

Service Descriptor Structure
(Not the full path used in ExecStart, this is important!)
'''
[Unit]

Description=Led Service Test

After=network.target

[Service]

Type=simple
#Type=forking
#PIDFile=/var/run/ledtest.pid

WorkingDirectory=/home/pi/apps/systemd/
ExecStart=/usr/bin/python /home/pi/apps/systemd/ledtest.py
KillMode=process
#RemainAfterExit=true

[Install]

WantedBy=multi-user.target
'''
