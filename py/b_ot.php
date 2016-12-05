
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
        print "<FRAMESET ROWS='40%,60%' FRAMEBORDER=yes>\n";
        print "  <FRAME SRC='_pname.php?act=input' name='input'>\n";
        print "  <FRAME SRC='_pname.php?act=display' name='body'>\n";
        print "</FRAMESET>\n";

}

function db_conn()
  {
     $db = mysql_connect('_dbhost','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
?>

