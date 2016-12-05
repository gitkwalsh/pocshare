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
            mampi
        }
        print "</table>";
