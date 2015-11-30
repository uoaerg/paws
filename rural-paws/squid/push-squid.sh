#!/bin/sh

squid -k rotate

cat /var/logs/access.log.0 | while read LINE
do
    echo wget -O - http://paws-man.erg.abdn.ac.uk/submit.php?l=`echo $LINE | sed -f url.sed` > /dev/null &
done

rm -f /var/logs/access.log.0

