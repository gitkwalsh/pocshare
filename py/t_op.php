<?php
switch ($_REQUEST['act'])
  {
     case "update":
         tb_update( $_REQUEST['id']);
         break;
     case "edit":
         tb_edit( $_REQUEST['id']);
         break;
     case "input":
         tb_input();
         break;
     case "insert":
         tb_insert();
         break;
       case "display":
         tb_display();
         break;
       case "start":
         f_start('unose');
         break;
         }
#-------------------------------------
