#!/bin/bash

delete(){
    ampy --port /dev/ttyUSB0 rm $1
}

put(){
    ampy --port /dev/ttyUSB0 put $1
}

replace(){
    echo "Working on $1"
    delete $1
    put $1
}

replace boot.py
replace main.py
replace app.py
replace helpers.py