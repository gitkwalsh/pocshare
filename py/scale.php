<?php
switch ($_REQUEST['act'])
  {
     case "insert":
         pick_in();
         break;
     case "scaleup":
         cdeploy();
         break;
       case "delete":
         cdelete();
         break;
         }



function tb_update()
{


	$id = $_REQUEST['id'];
	$ipaddress = $_REQUEST['ipaddress'];
	$contextid = $_REQUEST['contextid'];
	$componetid = $_REQUEST['componetid'];
	$nsvrcount = $_REQUEST['nsvrcount'];
	$svrmax = $_REQUEST['svrmax'];
	$status = $_REQUEST['status'];
 	$v_query = "update  scale set  ipaddress =$_REQUEST["ipaddress"]', contextid =$_REQUEST["contextid"]', componetid =$_REQUEST["componetid"]', nsvrcount =$_REQUEST["nsvrcount"]', svrmax =$_REQUEST["svrmax"]', status =$_REQUEST["status"]', where id = $_REQUEST['id'];
  
 	f_sqlex($v_query);
}
}#==========================================================

function tb_input ()
{

	<table border=1> <form action=%s.php ><input type=hidden name=act value=_insert>
	<tr><td>ipaddress</td><td><input type=text name=ipaddress></td></tr>
	<tr><td>contextid</td><td><input type=text name=contextid></td></tr>
	<tr><td>componetid</td><td><input type=text name=componetid></td></tr>
	<tr><td>nsvrcount</td><td><input type=text name=nsvrcount></td></tr>
	<tr><td>svrmax</td><td><input type=text name=svrmax></td></tr>
	<tr><td>status</td><td><input type=text name=status></td></tr>
	<tr><td></td><td><input type=submit value=insert></td></tr>
#==========================================================

function tb_insert()
{

	$ipaddress = $_REQUEST['ipaddress'];
	$contextid = $_REQUEST['contextid'];
	$componetid = $_REQUEST['componetid'];
	$nsvrcount = $_REQUEST['nsvrcount'];
	$svrmax = $_REQUEST['svrmax'];
	$status = $_REQUEST['status'];
 
	$v_query = "insert into scale (ipaddress,contextid,componetid,nsvrcount,svrmax,status)  values ('$ipaddress','$contextid','$componetid','$nsvrcount','$svrmax','$status');"
 

	  f_sqlex($v_query);
}
#==========================================================

function tb_display()
{

	$v_query = "select * from scale ";
'<tr><td>$srow[0]</td>';'<tr><td>$srow[1]</td>';'<tr><td>$srow[2]</td>';'<tr><td>$srow[3]</td>';'<tr><td>$srow[4]</td>';'<tr><td>$srow[5]</td>';  
}#==========================================================


function f_sqlex($v_sql)
  {
    $v_eqry   = $v_sql;
        $my_esdb  = db_conn();
        $v_eresult = mysql_query($v_eqry,$my_esdb) or print('Query failed: ' . mysql_error());
    $ret = $v_eresult;
    #mysql_free_result($v_eresult);
    mysql_close($my_esdb);
    return $ret;
  }

function db_conn()
  {
     $db = mysql_connect('hptools.myhome2k.org','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
?>


