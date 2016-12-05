<?php

ttry();
function ttry()
 { 
		$act1 =  $_request["act1"];
		$act2 =  $_request["act2"];
		$hbuf = "<html><head><link href='csa.css' type='text/css' media='screen' rel='stylesheet' /></head>";
		print(hbuf);


        if ($act1 =="edit" )
		  {
		    
			$dsql_a = "";
			 
			$id   =  $_request["id"];
			$dsql_a = "select id, pvalue,pdisplay,pdesc,ptype,ptype1 from picklist where id ="+ $id ;
			$buf_a = "<form name = edit action='mgmtpicklist.jsp' method='post'><input type=hidden name=act1 value='eupdate'><input type=hidden name=id value=" + $id +"> <input type=hidden name=act2 value='at'>";
            $v_query=$dsql_a;
			$my_sdb  = db_conn();
			$v_sresult = mysql_query($v_query,$my_sdb);
			  $buf_a =  $buf_a + "<table border=1>";
			  $buf_a =  $buf_a + "<tr><td>Value</td><td><input type=text name ='pvalue'    value="+ rs.getString(2) + "> </td></tr>";
			  $buf_a =  $buf_a + "<tr><td>Display Value</td><td><input type=text name=pdisplay value="+ rs.getString(3) + "> </td></tr>";
			  $buf_a =  $buf_a + "<tr><td>Description</td><td><input type=text name=pdesc value="+ rs.getString(4) + "> </td></tr>";
			 
			  $buf_a =  $buf_a + "<tr><td>Ptype</td><td><input type=text name ='ptype'     value="+ rs.getString(5) + "> </td></tr>";
			  $buf_a =  $buf_a + "<tr><td>Ptype1</td><td><input type=text name ='ptype1'   value="+ rs.getString(6) + "  > </td></tr>";
			 
			 
			 
			  $buf_a =  $buf_a + "<tr><td colspan=2 align=right><input type=submit value=Update></td> </tr>";
			  $buf_a =  $buf_a + "</table>";
			  
			 
			 $buf_a =  $buf_a ;
			print( $buf_a);
		 }

		 
        if ($act1 =="Add"  )
		  {
		    
			$dsql_a = "";
            $dsql_a = "select distinct ptype from csadata.picklist order by 1";
			ResultSet $rs=st.executeQuery($dsql_a);
			$buf_a = "<form name = addit action='mgmtpicklist.jsp' method='post'><input type=hidden name=act1 value='insert'> <input type=hidden name=act2 value='insert'>";
			$buf_a =  $buf_a + "";
			$sel = "<select name=ptype>";
			while (rs.next())
			 {
			  $sel =$sel + "<option value='" + rs.getString(1) +"'>"+ rs.getString(1) +"</option>";
			    
			 }
			$sel=sel + "</select>";
			  $buf_a =  $buf_a + "<table border=1>";
			  $buf_a =  $buf_a + "<tr><th colspan=2>Enter New picklist option</th></tr>";
			  $buf_a =  $buf_a + "<tr><td>Type</td><td>" +$sel +"<br>" ;
			  $buf_a =  $buf_a + "New Type:<input type=text name=nptype value=''></td></tr>";
			  $buf_a =  $buf_a + "<tr><td>Ptype1</td><td><input type=text name ='ptype1'> </td></tr>";
			 
			  $buf_a =  $buf_a + "<tr><td>Value</td><td><input type=text name ='pvalue'> </td></tr>";
			  $buf_a =  $buf_a + "<tr><td>Display Value</td><td><input type=text name=pdisplay > </td></tr>";
			  $buf_a =  $buf_a + "<tr><td>Description</td><td><input type=text name=pdesc > </td></tr>";
			  $buf_a =  $buf_a + "<tr><td colspan=2 align=right><input type=submit value=Save></td> </tr>";
			  $buf_a =  $buf_a + "</table>";
			  
			 
			 $buf_a =  $buf_a ;
			print( $buf_a);
		 }
        if ($act1 =="insert" )
		  {
				
			$pvalue   =  $_request["pvalue");
			$ptype    =  $_request["ptype");
			$ptype1    =  $_request["ptype1");
			$nptype    =  $_request["nptype");
			$pdisplay =  $_request["pdisplay");
			$pdesc    =  $_request["pdesc");
			$dsql_a   = "";
			if ($nptype =="" ) 
			 {
			  //nada
			 }
			 else
			  {
			    $ptype = $nptype;
			  }
			$dsql_a = "insert into picklist (ptype,pvalue,pdisplay,pdesc,ptype1) values ('" + $ptype + "','" + $pvalue + "','" + $pdisplay + "','" + $pdesc + "','" +$ptype1 +"')"  ;
			//print(dsql_a);
			
			st.executeUpdate(dsql_a);
			$act1 = "list"; 
		 }

       if ($act1 =="eupdate" )
		  {
				
			$id    =  $_request["id");
			$pvalue   =  $_request["pvalue");
			$ptype    =  $_request["ptype");
			$ptype1    =  $_request["ptype1");
			 
			$pdisplay =  $_request["pdisplay");
			$pdesc    =  $_request["pdesc");
			$dsql_a   = "";

			$dsql_a = "update picklist set pvalue = '" + $pvalue + "',ptype='" + $ptype + "',ptype1='" + $ptype1 + "',pdisplay='" +$pdisplay  +"' where id =" + $id ;
			print($dsql_a);
			
			st.executeUpdate($dsql_a);
			$act1 = "list"; 
		 }		 

        if ($act1 =="update" )
		  {
				
			$pvalue   =  $_request["pvalue");
			$ptype    =  $_request["ptype");
			$ptype1    =  $_request["ptype1");
			$nptype    =  $_request["nptype");
			$pdisplay =  $_request["pdisplay");
			$pdesc    =  $_request["pdesc");
			$dsql_a   = "";
			if ($nptype =="") ) 
			 {
			  //nada
			 }
			 else
			  {
			    $ptype = $nptype;
			  }
			$dsql_a = "insert into picklist (ptype,pvalue,pdisplay,pdesc,ptype1) values ('" + $ptype + "','" + $pvalue + "','" + $pdisplay + "','" + $pdesc + "','" +$ptype1 +"')"  ;
			//print(dsql_a);
			
			st.executeUpdate(dsql_a);
			$act1 = "list"; 
		 }

		 
		
		if ($act1 =="list" )
		  {
		    $cat =" ";
			$dsql = "";
            $dsql = "select id,pvalue,pdisplay,pdesc,ptype,ptype1 from picklist order by ptype,ptype1,pvalue"; 
			 
			ResultSet rs=st.executeQuery(dsql);
			
			$buf = "<a href='mgmtpicklist.jsp?act1=Add&act2=add&id=0'>Add</a><table border=1>";
			
			while (rs.next())
			 {
			   $buf = $buf + "<tr><td>" + rs.getString(5) + "</td><td>" + rs.getString(6) +"</td><td>" + rs.getString(2) + "</td><td>" + rs.getString(3) +"</td>";
			   $buf = $buf + "<td>" + "<a href='mgmtpicklist.jsp?act1=edit&act2=add&id=" +rs.getString(1)+"'>E</a>dit</td></tr>";
			 }
			$buf = $buf + "</table>";
			print(buf);
		 }
    }

function db_conn()
  {
     $db = mysql_connect('hptools.myhome2k.org','csauser','pwcsauser');
     mysql_select_db('csadata',$db);
     return $db;
  }
  
