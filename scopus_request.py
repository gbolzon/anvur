import os,json
from openpyxl import load_workbook, Workbook
import urllib

class scopus_paper():
    def __init__(self,scopus_id, title, scopus_cit, journal):
        self.scopus_id=scopus_id
        self.scopus_title=title
        self.scopus_citations=scopus_cit
        self.journal=journal
        

def trunk_string(inputstring,n):
    words = inputstring.rsplit(" ")
    L=""
    for word in words:
        if len(L)+len(word) >n : break
        L +=word
        L +=" "
    return L
    

def search_by_title(title):
    encoded_title=urllib.quote(title)#title.replace(" ","%20")
    
    os.system("./request_by_title.sh " + encoded_title)
    
    fid=open('a.json','r') 
    A=json.load(fid)  # list of dicts
    fid.close()
    
    entries=A['search-results']['entry']
    nfoundPapers= len(entries)
    PAPERLIST=[]
    for ip in range(nfoundPapers):
        scopus_id=entries[ip]['prism:url'].rsplit("/")[-1]
        scopus_cit =int(entries[ip]['citedby-count'])
        scopus_title=entries[ip]['dc:title']
        journal = entries[ip]['prism:publicationName']
        P =  scopus_paper(scopus_id, scopus_title,scopus_cit,journal)
        PAPERLIST.append(P)
    return PAPERLIST


title="Imaging of the Dinaric-Alpine chain convergence zone"
#print citations(title)

book = load_workbook(filename="sample.xlsx", read_only=False,data_only=False)
sheet=book['Sheet']

avoid_list=["CO2","("]

for ip in range(15,30):
    xls_row= ip + 11
    strTitle = "J%d" %(xls_row)
    title=sheet[strTitle].value
    ntrunk=150
    for bad_string in avoid_list:
        n_bad= title.find(bad_string)
        if (n_bad > -1 ) & ( n_bad < ntrunk):
            ntrunk = n_bad

    try:
        P = search_by_title(trunk_string(title,ntrunk))
    except:
        print "NOT FOUND " + title
    print P[0].scopus_citations, title