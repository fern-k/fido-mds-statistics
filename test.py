import json

file_path = 'test.txt' 

with open(file_path, 'r') as file:
    file_content = file.read()

json_data = json.loads(file_content)

from cryptography import x509
from cryptography.hazmat.backends import default_backend
import base64

def decode(strs):
    issuer_list = []
    for sstr in strs:
        base64_cert = (sstr
        )
        decoded_cert = base64.b64decode(base64_cert)
        try:
            cert = x509.load_der_x509_certificate(decoded_cert, default_backend())
            issuer = cert.issuer
            issuer_list.append(issuer)
        except:
            issuer_list.append("None")
    return issuer_list

import re
import pandas as pd
all_df = pd.DataFrame(index=[],columns=['is fido sepcial','authenticator description','issuer detail'])
tps = json_data['entries']
for tp in tps:
    if len(tp['metadataStatement']['attestationRootCertificates'])!=0:
        issuer_list = decode(tp['metadataStatement']['attestationRootCertificates'])
        is_fido = ["fido" in str(s).lower() for s in issuer_list]
        tmp = pd.DataFrame({
                            'is fido sepcial':is_fido,
                            'authenticator description':[tp['metadataStatement']['description']]*len(issuer_list),
                            'issuer detail':issuer_list, 
                        })
    all_df = pd.concat([all_df, tmp], ignore_index=True)
all_df.drop_duplicates(inplace=True)

all_df.to_csv("fido.csv")



print(f"cannot decode x5c:{(all_df['issuer detail']=='None').mean()}")
print(f"root cert is fido sepcial:{(all_df['is fido sepcial']==True).mean()}")