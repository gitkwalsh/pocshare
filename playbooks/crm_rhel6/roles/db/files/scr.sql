CREATE USER 'scrm'@'localhost' IDENTIFIED BY 'pwscrm'; 
GRANT ALL PRIVILEGES ON *.* TO 'scrm'@'localhost' WITH GRANT OPTION; 
CREATE USER 'scrm'@'%' IDENTIFIED BY 'pwscrm'; 
GRANT ALL PRIVILEGES ON *.* TO 'scrm'@'%' WITH GRANT OPTION; 
