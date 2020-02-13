import os, glob
from hlcrud import HlCrud

import pandas as pd
import csv

hlcrud = HlCrud("config.ini")

print('Successfully started...')

for filename in os.listdir(os.getcwd() + '/csv'):
    data = {'col{}'.format(v+1): k for v, k in enumerate(os.path.splitext(filename)[0].split('_'))}
    hlcrud.insert('filenames', data)
    hlcrud.show('filenames')

    with open(os.getcwd() + '/csv/' + filename) as csvfile:
        csv_data = csv.reader(csvfile, delimiter=",")
        next(csv_data)
        headers=['BoardSN', 'CompName', 'Type', 'cModel', 'DLinference_result', 'directory', 'ConfirmDefect', 'MachineDefect', 'Status', 'image_name', 'LightingCondition', 'image_scantime', 'BoardRESULT']
        for row in csv_data:
            data = {'{}'.format(headers[v]): k for v, k in enumerate(row)}
            hlcrud.insert('boards', data)
        hlcrud.show('boards')
