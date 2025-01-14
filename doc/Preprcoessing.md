# Preprocessing

The original images were in .C01 microcopic format stored on (Swestore)[https://docs.swestore.se/]


## Access to Swestore

For accessing Swestore, we have used two tools.

First, we have used lftp through terminal: 
```bash
lftp
```

```bash
get plate_number.tar.gz
```
for downloading whole plate or 

```bash
put plate_number.tar.gz
```
for uploading files.


