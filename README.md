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
  - **help command**<p>
  hl-crud.py -h
  - **show all data**<p>
  hl-crud.py -s show -t data
  - **insert data**<p>
  insert_data = {....}
  hl-crud.py -s insert -t data -w insert_data
  - **delete data**<p>
  hl-crud.py -s delete -t data -w CompName='aaa'
  - **search data**<p>
  hl-crud.py -s search -t data -w CompName='aaa'
  
  
