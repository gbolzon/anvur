import os,json
from openpyxl import load_workbook, Workbook
import urllib

class scopus_paper():
    def __init__(self,scopus_id, title, scopus_cit, journal):
        self.scopus_id=scopus_id
        self.scopus_title=title
        self.scopus_citations=scopus_cit
        self.journal=journal
    def __repr__(self):
        toprint=(self.scopus_id,self.scopus_citations,self.journal, self.scopus_title)
        l ="SCOPUS_ID : %s\n"
        l+="CITATIONS : %s\n"
        l+="JOURNAL   : %s\n"
        l+="TITLE     : %s\n"
        return l % toprint

def trunk_string(inputstring,n):
    inputstring=inputstring.replace('?','')
    words = inputstring.rsplit(" ")
    L=""
    for word in words:
        if len(L)+len(word) >n : break
        L +=word
        L +=" "
    return L
    

def search_by_title(title):
    '''
    returns a list of Scopus_Paper Objects
    '''
    encoded_title=urllib.quote(title)
    
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



book = load_workbook(filename="Anvur_2020_21_OGS.xlsx", read_only=False,data_only=False)
sheet=book['Foglio1']

avoid_list=["(","?"]

for ip in range(867):
    xls_row= ip + 12
    strTitle = "O%d" %(xls_row)
    str_id   = "P%d" %(xls_row)
    str_cit  = "Q%d" %(xls_row)
    str_rew  = "R%d" %(xls_row)
    str_undef= "S%d" %(xls_row)


    scopus_id = int(sheet[str_id].value)
    if scopus_id != 0 : continue  # scopus_id = 0 means still not calculated

    title=sheet[strTitle].value.replace('CO2','').replace("?","").replace("(","").replace(")","")
    ntrunk=150

    for bad_string in avoid_list:
        n_bad= title.find(bad_string)
        if (n_bad > -1 ) & ( n_bad < ntrunk):
            ntrunk = n_bad

    success=False
    try:
        Paperlist = search_by_title(trunk_string(title,ntrunk))
        success = True

    except:
        print "NOT FOUND " + title

    if success :
        print title
        if len(Paperlist) > 1:
            sheet[str_undef] = 'undefined'
            print "More than one title found"
        p=Paperlist[0]
        sheet[str_id]  = p.scopus_id
        sheet[str_cit] = p.scopus_citations
        sheet[str_rew] = p.journal

book.save("sample2.xlsx")
