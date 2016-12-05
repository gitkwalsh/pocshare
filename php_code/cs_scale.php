<?php
switch ($_REQUEST['act'])
  {
     case "insert":
         tb_insert();
         break;
     case "scaleup":
         scaleup();
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
 

function scaleup()
{
        $ipaddress = $_REQUEST['ipaddress']; 
        $v_query = "select concat(contextid,',',componetid) from csadata.scale  where ipaddress ='$ipaddress';";
        $my_sdb  = db_conn();
        $v_sresult = mysql_query($v_query,$my_sdb);
        if (!$v_sresult) 
          {
           echo 'Could not run query: ' . mysql_error($my_sdb );
            #exit;
          }
        $srow= mysql_fetch_row($v_sresult);
        print "$srow[0]";
}


function tb_insert()
{

        $ipaddress = $_REQUEST['ipaddress'];
        $contextid = $_REQUEST['contextid'];
        $componetid = $_REQUEST['componetid'];
        $nsvrcount = $_REQUEST['nsvrcount'];
        $svrmax = $_REQUEST['svrmax'];
        $status = $_REQUEST['status'];
        $v_query = "insert into scale (ipaddress,contextid,componetid,nsvrcount,svrmax,status)  values ('$ipaddress','$contextid','$componetid','$nsvrcount','$svrmax','$status');";
        f_sqlex($v_query);
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
