Reset everyone's passwords.


Run:

```
python list-users.py $API_KEY > everyone.txt
```


Then run:

```
python reset-passwords.py everyone.txt
```
