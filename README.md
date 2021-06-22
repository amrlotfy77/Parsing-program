## Parsing-program
### clone steps

**clone project files into input_data : -**
```
git init

git remote add origin https://github.com/amrlotfy77/Parsing-program.git

git pull origin main

``` 
 **install requirements.txt steps** 
 ( linux ubuntu )
```
python3 -m venv venv

pip install -t requirements.txt

. ./venv/bin/activate
```
**access branches** 

```
git checkout Feature1
git checkout Feature2
git checkout Feature3
```

then change file
permissions to run directly

```
chmod +x parser.py

```

run parser.py for xml parsing

```
./parser.py xml xml/file1.xml 

```

run parser.py for csv parsing

```
./parser.py csv csv/customers_file1.csv csv/vehicles_file1.csv

```