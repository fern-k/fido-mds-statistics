# FIDO MDS  STATISTICS

### Files Description

- [test.py](https://github.com/fern-k/fido-mds-statistics/blob/main/test.py)：A python script that reads json dictionary data in test.txt and collects statistics on the root certificate information in the FIDO MDS.
- [test.txt](https://github.com/fern-k/fido-mds-statistics/blob/main/test.txt)：The result of parsing the blob.jwt file by the jwt tool.
- [fido.csv](https://github.com/fern-k/fido-mds-statistics/blob/main/fido.csv)：The final parsing result includes whether the FIDO annotation is present, the authenticator description, and the issuer detail.

### Run Approach

```
python test.py
```

