#! /bin/sh

export PYTHONPATH=$PYTHONPATH:../
make html
make latexpdf

cp -r _build/html/* ../doc/ 
