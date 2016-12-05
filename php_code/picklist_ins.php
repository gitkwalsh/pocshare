<?php
switch ($_REQUEST['act'])
  {
     case "insert":
         pick_in();
         break;
     case "deploy":
         cdeploy();
         break;     
       case "delete":
         cdelete();
         break; 
         }         

   
  function cdelete()
{
    $dsql ="";
    
    $pvalue =   $_REQUEST['pvalue'];
    
    $dsql = "delete from csadata.picklist   where pvalue='$pvalue';";
    #print $dsql;
    f_sqlex($dsql);
}


 
  function cdeploy()
{
    $dsql ="";
    
    $pvalue =   $_REQUEST['pvalue'];
	$ptype1 =   $_REQUEST['ptype1'];
    
    $dsql = "update csadata.picklist set ptype1 ='$ptype1' where pvalue='$pvalue';";
    #print $dsql;
    f_sqlex($dsql);

}
function pick_in()
{
    $dsql ="";
    
    $pvalue =   $_REQUEST['pvalue'];
    $pdisplay =   $_REQUEST['pdisplay'];
    $ptype =   $_REQUEST['ptype'];
    $pdesc =   $_REQUEST['pdesc'];
	$ptype1 =   $_REQUEST['ptype1'];
    
    $dsql = "insert into csadata.picklist (pvalue,pdisplay,ptype,ptype1,pdesc) values ";
    $dsql = $dsql . "('$pvalue','$pdisplay','$ptype','$ptype1','$pdesc');";
    print $dsql;
    f_sqlex($dsql);

}
     
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
