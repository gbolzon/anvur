from commons.utils import file2stringlist
from scholarly import scholarly
import numpy as np
YEARS=range(2016,2022)
nYears=len(YEARS)

statistics=['citedby','hindex','i10index', 'citedby5y','hindex5y','i10index5y','cit2016','cit2017','cit2018','cit2019','cit2020','cit2021']
#my_dtype=[('Name', 'S100')]
my_dtype =[(s,np.int) for s in statistics] 


OGS_NAMES=file2stringlist('ogs.txt')
#OGS_NAMES=['Giorgio Bolzon', 'Laura Mariotti','Edy Forlin']

def get_author_statistics(name):
    OUT=np.zeros((1,),dtype=my_dtype)
    search_query=scholarly.search_author(name)#
    author = scholarly.fill(next(search_query))
    for s in statistics[:6]:
        OUT[s] = author[s]
    
    for year in YEARS:
        yearstr="cit%s" %(year)
        try:
            OUT[yearstr] = author['cites_per_year'][year]
        except:
            pass

    
    return OUT
    



nAuthors=len(OGS_NAMES)
A = np.zeros((nAuthors,1), dtype=my_dtype)
for iname, name in enumerate(OGS_NAMES):
    print(name)
    try:
        A[iname,0] = get_author_statistics(name+  ", OGS")
    except:
        A[iname,0] = get_author_statistics(name)
    
    if A[iname,0 ][0] == 0: print("############# Error in  " + name)

header='citazioni \t h index \t i10 index '



fid = open('ogs_scholar.txt','wt')
for iname, name in enumerate(OGS_NAMES):
    fid.write(name + "\t")
    np.savetxt(fid, A[iname], fmt="%d", delimiter="\t")
fid.close()

#np.savetxt('ogs_scholar.txt', A,  fmt = fmt, header=header)

#from commons.utils import writetable
#rows_names_list=OGS_NAMES
#column_names_list=statistics
#writetable('ogs_scholar.txt', B, rows_names_list, column_names_list, "%d")

# 
#     search_query=scholarly.search_author(name)
#     author = scholarly.fill(next(search_query))
#     
#     all_citations=author['citedby']
#     print(author['citedby5y'] )
#     
#     
#     i10index=author['i10index'] 
#     i10index_5years=author['i10index5y']
#     hindex = author['hindex']
#     hindex_5years = author['hindex5y']
#     
#     citations_from_2016=np.zeros((nYears),np.int)
#     
#     
#     for iyear,year in enumerate(YEARS):
#         citations_from_2016[iyear] = author['cites_per_year'][year]
#     
    




