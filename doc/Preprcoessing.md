# Preprocessing

The original images were in .C01 microcopic format stored on (Swestore)[https://docs.swestore.se/]


## Access to Swestore

For accessing Swestore, we have used two tools.

First, we have used lftp through terminal: 
```bash
lftp https://username@webdav.swestore.se/snic/folder/
```

For downloading whole plate we used:
```bash
get plate_number.tar.gz
```

For uploading files we have used:
```bash
put plate_number.tar.gz
```

The other way to access files on Swestore was winscp tool which is a win-based tool.


![WinSCP](_static/WinSCP.png)