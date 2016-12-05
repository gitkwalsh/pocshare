<?php
switch ($_REQUEST['act'])
  {
     case "input":
         tb_input();
         break;
     case "insert":
         tb_insert();
         break;
       case "display":
         tb_display();
         break;
       case "start":
         f_start('unose');
         break;
         }
#-------------------------------------

function tb_input ()
{

	print '<table border=1> <form action=unosee.php ><input type=hidden name=act value=insert>';
	print '<tr><td>topic</td><td><input type=text name=topic></td></tr>';
	print '<tr><td>dkey</td><td><input type=text name=dkey></td></tr>';
	print '<tr><td>dstuff</td><td><input type=text name=dstuff></td></tr>';
	print '<tr><td>dstuff2</td><td><input type=text name=dstuff2></td></tr>';
	print '<tr><td></td><td><input type=submit value=insert></td></tr>';

}#==========================================================

function tb_insert()
{

	$topic = $_REQUEST['topic'];
	$dkey = $_REQUEST['dkey'];
	$dstuff = $_REQUEST['dstuff'];
	$dstuff2 = $_REQUEST['dstuff2'];
 
	$v_query = "insert into unosee (topic,dkey,dstuff,dstuff2) values ('$topic','$dkey','$dstuff','$dstuff2');";


	  f_sqlex($v_query);
}
#==========================================================

function tb_display()
{

	$v_query = "select * from unosee ";
        $my_sdb  = db_conn();
        $v_sresult = mysql_query($v_query,$my_sdb);
        if (!$v_sresult) 
          {
           echo 'Could not run query: ' . mysql_error($my_sdb );
            #exit;
          }
        $n_rows = mysql_num_rows($v_sresult);
        print "<form action='w.php' method='post'>";
        print "<input type='hidden' name='v_action' value='add'>";
        print " <table border=1>";
        while( $srow= mysql_fetch_row($v_sresult))
        {
            
		print '<tr><td>'.$srow[0].'</td><td>'.$srow[1].'</td><td>'.$srow[2].'</td><td>'.$srow[3].'</td></tr>';

        }
        print "</table>";
  
}
#==========================================================


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


