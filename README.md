# hl-crud
Python module for CRUD module - Python3 | MySQL | Docker

## Installation
  ~~~
    sudo sh setup.sh
  ~~~

## How to run docker image
  ~~~
    docker-compose build --no-cache
    docker-compose up
  ~~~

## Command Usage
  ~~~
    hl-crud.py -s [command] -t [tablename] -d [data] -w [where]
  ~~~

## Examples
  - **help command**<p>
  ~~~
    hl-crud.py -h
  ~~~
  - **show command**<p>
  ~~~
    hl-crud.py -s show -t boards
    hl-crud.py -s show -t filenames
  ~~~
  - **insert command**<p>
  data = {...}
  ~~~
    hl-crud.py -s insert -t boards -d '{"BoardSN":123,"CompName:"Fesv","Result":"Pass", ...}'
    hl-crud.py -s insert -t filenames -d '{"col1":"AAAA","col2:"BBB-C1234-D123-E12345~FOT","col3":"G16149190021","col4":"ILAOI-B","col5":"20200204195425"}'
  ~~~
  - **delete command**<p>
  ~~~
    hl-crud.py -s delete -t boards -w CompName='aaa'
  ~~~
  - **select command**<p>
  ~~~
    hl-crud.py -s select -t boards -w CompName='aaa'
  ~~~
  - **update command**<p>
  ~~~
    hl-crud.py -s update -t boards -d '{"BoardSN":123,"CompName:"Fesv","Result":"Pass", ...}' -w CompName='aaa'
  ~~~

  
