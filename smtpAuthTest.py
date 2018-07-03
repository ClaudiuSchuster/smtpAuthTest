#!/usr/bin/python

import argparse
import smtplib
import socket

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tests SMTP-Login')
    parser.add_argument('--username', '-u', dest='username', action='store', help='Username')
    parser.add_argument('--password', '-p', dest='password', action='store', help='Password')
    parser.add_argument('--host', '-H', required=True, dest='host', action='store', help='SMTP Hostname')
    parser.add_argument('--port', '-P', dest='port', action='store', help='optional SMTP Port', default='25')
    parser.add_argument('--tls', '-t', dest='tls', action='store_true', help='optional Use TLS')
    parser.add_argument('--sender', '-s', dest='sender', action='store', help='optional TestMail-Sender', default='SmtpAuthTest@'+socket.gethostname())
    parser.add_argument('--receiver', '-r', dest='receiver', action='store', help='Send TestMail to Receiver')

    args = parser.parse_args()

    server = smtplib.SMTP(args.host, int(args.port))
    server.set_debuglevel(1)
    if args.tls:
        server.ehlo()
        server.starttls()
    server.ehlo()
    if args.username and args.password:
        server.login(args.username, args.password)
    if args.receiver:
        server.sendmail(args.sender, [args.receiver], 'SmtpAuthTest@'+socket.gethostname())
    server.quit()

    exit(0)
