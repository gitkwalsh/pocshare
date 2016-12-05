<%@ page import="java.sql.*,java.net.*,java.io.*,java.lang.*,java.util.*"%>
<%
try{
     String ptype =  request.getParameter("ptype");
     String ptype1 =  request.getParameter("ptype1");
     String rtype =  request.getParameter("rtype");
     String surl = "http://192.168.136.65/scripts/t2.php?ptype=" + ptype + "&rtype=" + rtype + "&ptype1=" + ptype1  ;
    URL oracle = new URL(surl);
    BufferedReader in = new BufferedReader(
    new InputStreamReader(oracle.openStream()));

    String inputLine;
    while ((inputLine = in.readLine()) != null)
        out.println(inputLine);
    in.close();
    }catch(Exception ex){}
%> 