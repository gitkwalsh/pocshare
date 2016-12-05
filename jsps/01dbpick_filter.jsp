<%@ page import="java.sql.*,java.net.*,java.io.*,java.lang.*,java.util.*"%>
<%
try{
    String ptype =  request.getParameter("ptype");
    String rfilter =  request.getParameter("filter");
    String surl = "http://192.168.136.65/scripts/tfilter.php?ptype=" + ptype + "&filter=" + rfilter ;
    URL oracle = new URL(surl);
    BufferedReader in = new BufferedReader(
    new InputStreamReader(oracle.openStream()));

    String inputLine;
    while ((inputLine = in.readLine()) != null)
        out.println(inputLine);
    in.close();
    }catch(Exception ex){}
%> 