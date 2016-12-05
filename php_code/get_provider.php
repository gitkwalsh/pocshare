<?php

csashow();

function csashow()
{
    $dsql ="";
    $type =   $_REQUEST['type'];
    $dsql = "select concat(displayname,',',accesspoint,',',userid,',',password) as provider from csadata.providers where type='$type'"; 
    $v_query = $dsql;
    #print $dsql;

    $my_sdb  = db_conn();
    $v_sresult = mysql_query($v_query,$my_sdb);
    if (!$v_sresult)
        {
        echo 'Could not run query: ' . mysql_error($my_sdb );
        #exit;
        }
       $srow= mysql_fetch_row($v_sresult);
       $buf = $srow[0];
        
    print $buf;

}
function db_conn()
  {
     $db = mysql_connect('localhost','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
?>
