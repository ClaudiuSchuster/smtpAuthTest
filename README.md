# smtpAuthTest.py

### ./smtpAuthTest.py -h
usage: smtpAuthTest.py [-h] [--username USERNAME] [--password PASSWORD] --host
                       HOST [--port PORT] [--tls] [--sender SENDER]
                       [--receiver RECEIVER]

Tests SMTP-Login

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME, -u USERNAME
                        Username
  --password PASSWORD, -p PASSWORD
                        Password
  --host HOST, -H HOST  SMTP Hostname
  --port PORT, -P PORT  optional SMTP Port
  --tls, -t             optional Use TLS
  --sender SENDER, -s SENDER
                        optional TestMail-Sender
  --receiver RECEIVER, -r RECEIVER
                        Send TestMail to Receiver
