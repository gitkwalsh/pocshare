CREATE USER 'csauser'@'localhost' IDENTIFIED BY 'pwcsauser'; 
GRANT ALL PRIVILEGES ON *.* TO 'csauser'@'localhost' WITH GRANT OPTION; 
CREATE USER 'csauser'@'%' IDENTIFIED BY 'pwcsauser'; 
GRANT ALL PRIVILEGES ON *.* TO 'csauser'@'%' WITH GRANT OPTION; 
