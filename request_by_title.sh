#! /bin/bash

TITLE=$1
curl --silent -H "X-ELS-APIKey:fb425047964708783b199856307c10ba"  "https://api.elsevier.com/content/search/scopus?query=TITLE($TITLE)" > a.json
#curl --silent -H "X-ELS-APIKey:fb425047964708783b199856307c10ba"  "https://api.elsevier.com/content/search/scopus?query=TITLE($TITLE)&field=citedby-count" > a.json
#curl --silent -H "X-ELS-APIKey:fb425047964708783b199856307c10ba"  "https://api.elsevier.com/content/search/scopus?query=TITLE($TITLE)&field=title" > b.json


KEY=fb425047964708783b199856307c10ba
#TITLE=Imaging%20of%20the%20Dinaric-Alpine%20chain%20convergence%20zone
#curl --verbose -H "X-ELS-APIKey:$KEY"  "https://api.elsevier.com/content/search/scopus?query=DOI(10.1016/j.stem.2011.10.002)&field=citedby-count"   > /Users/gbolzon/Downloads/pippo.txt


