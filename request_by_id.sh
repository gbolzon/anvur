#! /bin/bash

SCOPUS_ID=$1

KEY=fb425047964708783b199856307c10ba
curl --verbose -H "X-ELS-APIKey:$KEY" --header "Accept: application/json"  "https://api.elsevier.com/content/abstract/scopus_id/${SCOPUS_ID}"
exit 0

#curl --verbose -H "X-ELS-APIKey:$KEY"  "https://api.elsevier.com/content/article/entitlement?query=DOI(10.1016/j.stem.2011.10.002)"


curl --verbose -H "X-ELS-APIKey:$KEY"  "https://api.elsevier.com/content/search/scopus?query=DOI($DOI)"
