#!/bin/sh

wget -O /tmp/squid.conf http://paws-man.erg.abdn.ac.uk/squid.php
mv /tmp/squid.conf /etc/squid/
squid -k reconfigure

