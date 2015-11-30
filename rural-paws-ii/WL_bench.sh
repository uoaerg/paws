#script to automatically visit a list of urls and collect HAR files for page load time, onload time and tcp timings analysis
#configure the number i to correspond to the number of repeated visits

cat list.txt | while read LINE
do
i=1
while test $i -le "3"
	do   
		now=$(date +%Y%m%d%T)		
		echo $LINE  "\t time:$now"
		#echo "time:$now"
		export FIREFOX_START_REMOTE_CONTROL=1 
		echo window.location=\'$LINE\' | nc -q1 localhost 32000 &
		sleep 60	
		
		i=$((i+1))	
		echo "$i"		
	done
done
pkill firefox
	


