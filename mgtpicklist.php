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

	print '<table border=1> <form action=picklist.php ><input type=hidden name=act value=insert>';
	print '<tr><td>pvalue</td><td><input type=text name=pvalue></td></tr>';
	print '<tr><td>pdisplay</td><td><input type=text name=pdisplay></td></tr>';
	print '<tr><td>ptype</td><td><input type=text name=ptype></td></tr>';
	print '<tr><td>ptype1</td><td><input type=text name=ptype1></td></tr>';
	print '<tr><td>pdesc</td><td><input type=text name=pdesc></td></tr>';
	print '<tr><td></td><td><input type=submit value=insert></td></tr>';

}#==========================================================

function tb_insert()
{

	$pvalue = $_REQUEST['pvalue'];
	$pdisplay = $_REQUEST['pdisplay'];
	$ptype = $_REQUEST['ptype'];
	$ptype1 = $_REQUEST['ptype1'];
	$pdesc = $_REQUEST['pdesc'];
 
	$v_query = "insert into picklist (pvalue,pdisplay,ptype,ptype1,pdesc) values ('$pvalue','$pdisplay','$ptype','$ptype1','$pdesc');";


	  f_sqlex($v_query);
tb_display();
}#==========================================================

function tb_display()
{

	$v_query = "select * from picklist ";
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
            
		print '<tr><td>'.$srow[0].'</td><td>'.$srow[1].'</td><td>'.$srow[2].'</td><td>'.$srow[3].'</td><td>'.$srow[4].'</td></tr>';

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
function f_start($v_appname)
{
        print "<html><head><title>$v_appname</title></head>";
        print "<FRAMESET ROWS='20%,80%' FRAMEBORDER=yes>\n";
        print "  <FRAME SRC='picklist.php?act=input' name='input'>\n";
        print "  <FRAME SRC='picklist.php?act=display' name='bodu'>\n";
        print "</FRAMESET>\n";

}

function db_conn()
  {
     $db = mysql_connect('localhost','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
?>


