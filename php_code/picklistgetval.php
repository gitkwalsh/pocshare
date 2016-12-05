<?php
$pdisplay =   $_REQUEST['pdisplay'];
csashow();

function csashow()
{
    $dsql ="";
    $pdisplay =   $_REQUEST['pdisplay'];
    $dsql = "select pvalue from csadata.picklist where pdisplay='" . $pdisplay."'"; 
    $v_query = $dsql;
    #print $dsql;

    $my_sdb  = db_conn();
    $v_sresult = mysql_query($v_query,$my_sdb);
    if (!$v_sresult)
        {
        echo 'Could not run query: ' . mysql_error($my_sdb );
        #exit;
        }
        $n_rows = mysql_num_rows($v_sresult);
    while( $srow= mysql_fetch_row($v_sresult))
        {
        $buf = $srow[0];
        }
    print $buf;

}
function db_conn()
  {
     $db = mysql_connect('hptools.myhome2k.org','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
?>
