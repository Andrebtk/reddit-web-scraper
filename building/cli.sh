#!/bin/bash


echo "data :"
read data



if ["$data" = "test"]
then 
    echo "hell" 
fi

ssh pi@192.168.1.37 "cd memeBot ; DISPLAY=:0 python3 -c 'from function import *; print(dick())'"
