# -*- coding: utf-8 -*-


# Tested in Anaconda python
#

import sys
from xlrd import open_workbook

input_file = 'sales_2017.xlsx'

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print('Worksheet name:', worksheet.name, '\tRows:', 
          worksheet.nrows, '\tColumns:', worksheet.ncols)
    if worksheet.cols == 'Customer ID':
        print(worksheet.cols)