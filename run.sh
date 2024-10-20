#!/bin/bash

module="inventory.record"

for pid in `ps -aef | grep flask | grep -v grep | awk '{print $2}'`
do
   echo "killing process " $pid
   kill -9 $pid
done


export FLASK_APP=$module
export FLASK_ENV=development

python3 -m flask run -h localhost -p 5000 >> /tmp/$module-api.log 2>&1 &
#python3 -m flask run -h localhost -p 5000


