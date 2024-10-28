# install python

```
apt install python3 python3-pip -y
pip3 install psutil requests
mkdir /alert-como
cd /alert-como
git clone https://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@github.com/adymola/notifec2.git
python3 /alert-como/notifec2/storage.py
```

# change name

```
NAMAEC2 = 'EDIT'
```


# crontab

```
10 10 * * * python3 /alert-como/notifec2/storage.py
```
