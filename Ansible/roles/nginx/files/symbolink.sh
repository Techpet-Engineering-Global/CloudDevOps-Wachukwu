#!/usr/bin/bash

cd /etc/nginx/sites-enabled
if [[ -e site.conf ]]
then
    :
else
    ln -s ../sites-available/site.conf
fi
