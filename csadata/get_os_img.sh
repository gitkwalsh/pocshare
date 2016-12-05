#!/bin/bash
echo select pdisplay from csadata.picklist where pvalue=\""$1\""\; > /tmp/_geto.sql
mysql -ucsauser -ppwcsauser < /tmp/_geto.sql |grep -v pdisplay 
