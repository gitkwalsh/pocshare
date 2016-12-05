use csadata;
delete from picklist where ptype='DMA';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-none-","None","None","DMA","");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("wf_11g!dp_11g","11g Engine","11g Engine","DMA","");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("wf_orcl_instance!dp_orcl_instance","Instance-DB11","Instance-DB11","DMA","");

