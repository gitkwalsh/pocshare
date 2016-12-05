use csadata;
drop table IF EXISTS  unosee;
create table unosee (id MEDIUMINT NOT NULL AUTO_INCREMENT,topic varchar(40),dkey varchar(40),dstuff varchar(200),dstuff2 tinytext,PRIMARY KEY (id));
