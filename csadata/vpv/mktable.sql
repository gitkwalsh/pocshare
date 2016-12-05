use csadata;
drop table hpvm;
create table hpvm (id int NOT NULL AUTO_INCREMENT, vmid varchar(100) ,vmname varchar(50),cluster varchar(50),vmhost varchar(50),hyptype varchar(50),vm_managed varchar(50),managed_date datetime,vm_status varchar(20), subscriptionid varchar(80), primary key (id))
