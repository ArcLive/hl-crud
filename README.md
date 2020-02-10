# hl-crud
Python module for CRUD module - Python3 | MySQL | Docker

## Command Usage
  hl-crud.py -s 'crud type' -t 'table name' -w 'where or data'
  ### crud type
  insert, delete, show, search
  ### table name
  ### where or data
  - if crud type is "search" or "delete", use where condition
  - if crud type is "insert", use data.
## Examples
  - **help command**
  hl-crud.py -h
  - **show all data**
  hl-crud.py -s show -t data
  - **insert data**
  insert_data = {....}
  hl-crud.py -s insert -t data -w insert_data
  - **delete data**
  hl-crud.py -s delete -t data -w CompName='aaa'
  - **search data**
  hl-crud.py -s search -t data -w CompName='aaa'
  
  
