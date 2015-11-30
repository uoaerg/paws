<?php

mysql_connect('localhost', 'root', 'pawspassword');
mysql_select_db('paws');

/* Get the per device speed */
$q = "SELECT `value` FROM `global_settings` WHERE `key`='device_speed'";
$device_speed = mysql_fetch_array(mysql_query($q))[0];

/* Get the per link speed */
$q = "SELECT `value` FROM `global_settings` WHERE `key`='link_speed'";
$link_speed = mysql_fetch_array(mysql_query($q))[0];

/* Get the list of approved domains */
$approved_domains = [];
$q = "SELECT `domain` FROM `global_approved_domains`";
$r = mysql_query($q);
while ( ( $domain = mysql_fetch_array($r) ) != null ) {
	$approved_domains[] = $domain[0];
}

$settings = [];
$settings['device_speed'] = $device_speed;
$settings['link_speed'] = $link_speed;
$settings['approved_domains'] = $approved_domains;

echo json_encode($settings);

