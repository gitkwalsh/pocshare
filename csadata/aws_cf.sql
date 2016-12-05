use csadata;
delete from picklist where ptype='ASW_CF';
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("https://s3.amazonaws.com/mycf/cf_2tier_web_mariadb.template","cf_2tier_web_mariadb.template","cf_2tier_web_mariadb.template","ASW_CF","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("https://s3.amazonaws.com/mycf/cf_lamp.template","cf_lamp.template","cf_lamp.template","ASW_CF","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("https://s3.amazonaws.com/mycf/cf_lamp_6_tier.template","cf_lamp_6_tier.template","cf_lamp_6_tier.template","ASW_CF","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("https://s3.amazonaws.com/mycf/cf_mariadb_lb_web.template","cf_mariadb_lb_web.template","cf_mariadb_lb_web.template","ASW_CF","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("https://s3.amazonaws.com/mycf/pru_cf_lamp.template","pru_cf_lamp.template","pru_cf_lamp.template","ASW_CF","avail");
insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("https://s3.amazonaws.com/mycf/sugarcrm.template","sugarcrm.template","sugarcrm.template","ASW_CF","avail");

