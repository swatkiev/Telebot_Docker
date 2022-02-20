#!/bin/bash
cd /home/dockerbot
KILL=$(pgrep -f run.py); echo $KILL>/home/dockerbot/pid.txt; kill -9 $KILL
