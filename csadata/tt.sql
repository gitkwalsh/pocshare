use csadata;
delete from picklist where ptype='TPLATE';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("linux_template_001","Linux_Small","Linux_small","TPLATE","Linux");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("linux_template_004","Linux_Large","Linux_large","TPLATE","Linux");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("win_template_001","Windows_001","windows_001","TPLATE","Win");

