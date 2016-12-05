<?php

csashow();

function csashow()
{
    $dsql ="";
    $ptype =   $_REQUEST['ptype'];
    $rfilter =   $_REQUEST['filter'];

     $v_query = "select pvalue,  pdisplay,pdesc from csadata.picklist where ptype ='" .$ptype ."'"  . " and pdisplay like '%" . $rfilter ."%'" . " order by 1;";

     
    #print  $v_query;

    $my_sdb  = db_conn();
    $v_sresult = mysql_query($v_query,$my_sdb);
    if (!$v_sresult)
        {
        echo 'Could not run query: ' . mysql_error($my_sdb );
        #exit;
        }
        $n_rows = mysql_num_rows($v_sresult);
    $buf = "<Property>";
    while( $srow= mysql_fetch_row($v_sresult))
        {
        $buf = $buf . "<availableValues><value>" . $srow[0] ."</value><displayName>" . $srow[1] . "</displayName><description>" . $srow[2] . "</description></availableValues>";
        }
    $buf = $buf . "</Property>";
    print $buf;

}
function db_conn()
  {
     $db = mysql_connect('hptools.myhome2k.org','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
?>
