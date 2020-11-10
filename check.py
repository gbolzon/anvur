# at the moment checks only for double publications, on scopus_id

from openpyxl import load_workbook, Workbook
book = load_workbook(filename="Anvur_2020_21_OGS.xlsx", read_only=False,data_only=False)
sheet=book['Foglio1']

SCOPUS_ID_LIST=[]
XLS_ROW_LIST=[]

for ip in range(868):
    xls_row=ip+12
    str_id   = "P%d" %(xls_row)
    scopus_id=int(sheet[str_id].value)
    if scopus_id==0: continue
    if scopus_id in SCOPUS_ID_LIST:
        index=SCOPUS_ID_LIST.index(scopus_id)
        print "DUPLICATO", scopus_id, XLS_ROW_LIST[index] , xls_row

    else:
        SCOPUS_ID_LIST.append(scopus_id)
        XLS_ROW_LIST.append(xls_row)
    