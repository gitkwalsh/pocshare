use csadata;
delete from picklist where ptype = "SLA";
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-none-","none","none","SLA","");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("gold","Gold-Full Monitoring","none","SLA","");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("silver","Silver-Partial Monitoring","none","SLA","");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("bonze","Bronze-NO Monitoring","none","SLA","");
