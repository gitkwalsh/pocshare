       $my_sdb  = db_conn();
        $v_sresult = mysql_query($v_query,$my_sdb);
        if (!$v_sresult)
          {
           echo 'Could not run query: ' . mysql_error($my_sdb );
          }
         $srow= mysql_fetch_row($v_sresult);
