# hl-crud
Python module for CRUD module - Python3 | MySQL | Docker

## Installation
  ~~~
    sudo sh setup.sh
  ~~~

## How to run docker image
  ~~~
    docker-compose up
  ~~~

## Command Usage
  ~~~
    hl-crud.py -s 'crud type' -t 'table name' -w 'where or data'
  ~~~
  ### crud type
  insert, delete, show, search
  ### table name
  ### where or data
  - if crud type is "search" or "delete", use where condition
  - if crud type is "insert", use data.
## Examples
  - **help command**<p>
  ~~~
    hl-crud.py -h
  ~~~
  - **show all boards**<p>
  ~~~
    hl-crud.py -s show -t boards
  ~~~
  - **insert board**<p>
  data = {....}
  ~~~
    hl-crud.py -s insert -t boards -w <data>
    Ex] data={"BoardSN":123,"CompName:"Fesv","Result":"Pass"}
        hl-crud.py -s insert -t boards -w data
  ~~~
  - **delete board**<p>
  ~~~
    hl-crud.py -s delete -t boards -w CompName='aaa'
  ~~~
  - **search board**<p>
  ~~~
    hl-crud.py -s search -t boards -w CompName='aaa'
  ~~~
  
  
