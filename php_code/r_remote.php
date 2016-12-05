<?php
$host =   $_REQUEST['host'];

$stArray = explode("-",$host);
$c_type = $stArray[1];
$target = $stArray[0];
print "<meta http-equiv='content-type' content='text/html;charset=utf-8'/>";
print "<meta http-equiv='refresh' content='3;url=". $c_type . "://". $target ."'/>";
print "<script>function close_window() {  close();    } </script>";
print "</head><body background='http://192.168.136.65/backup/content/logos/login_background_color.jpg'><center><h2>Connecting to " . $target . "</h2><br>";
print "<table border=1><tr><td><img src='remote.gif'></td><td><img src='loading.gif'></td</tr></table>";
print  "<a href='a' onclick='close_window();return false;'>Close</a></center></body></html>";
?>
