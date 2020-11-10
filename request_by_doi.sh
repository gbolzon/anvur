#! /bin/bash

DOI=$1

KEY=fb425047964708783b199856307c10ba
#curl --verbose -H "X-ELS-APIKey:$KEY"  "https://api.elsevier.com/content/search/scopus?query=DOI(10.1016/j.stem.2011.10.002)&field=citedby-count" #   > /Users/gbolzon/Downloads/pippo.txt
#curl --verbose -H "X-ELS-APIKey:$KEY"  "https://api.elsevier.com/content/search/scopus?query=DOI(10.1016/j.stem.2011.10.002)"  > /Users/gbolzon/Downloads/pippo.txt

curl --verbose -H "X-ELS-APIKey:$KEY"  "https://api.elsevier.com/content/search/scopus?query=DOI($DOI)"
