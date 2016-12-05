use csadata;
delete from picklist where ptype='project';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("prog-1","prog-1","prog-1","project","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("prog-2","prog-2","prog-2","project","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("prog-3","prog-3","prog-3","project","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("prog-4","prog-4","prog-4","project","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-None-","-None-","-None-","project","avail");

use csadata;
delete from picklist where ptype='stage';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("DEV","DEV","DEV","stage","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("QA","QA","QA","stage","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("UAT","UAT","UAT","stage","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("PROD","PROD","PROD","stage","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-None-","-None-","-None-","stage","avail");

use csadata;
delete from picklist where ptype='costcenter';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-None-","-None-","-None-","costcenter","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("cc-2.1","cc-2.1","cc-2.1","costcenter","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("cc-2.2","cc-2.2","cc-2.2","costcenter","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("cc-2.3","cc-2.3","cc-2.3","costcenter","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("cc-3.1","cc-3.1","cc-3.1","costcenter","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("cc-3.2","cc-3.2","cc-3.2","costcenter","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("cc-3.4","cc-3.4","cc-3.4","costcenter","avail");

use csadata;
delete from picklist where ptype='owner';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-None-","-None-","-None-","owner","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("Marketing","Marketing","Marketing","owner","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("IT-Admin","IT-Admin","IT-Admin","owner","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("Developers","Developers","Developers","owner","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("SEC-Admin","SEC-Admin","SEC-Admin","owner","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("IT-Finance","IT-Finance","IT-Finance","owner","avail");

