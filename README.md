# Beaver

 **Beaver** is an open-source tool that lets you store usernames, passwords, and services. You can also customize it to save any other information you need. Its easy to use, quick to access from the terminal, and shows your data in a neat table. You can change it to fit your needs too.

 Right now, the tool doesnt **encrypt** the information it stores. Were working on adding encryption to keep your data safe on your device. If youre good at programming, you can help add this feature too. 
___
## How to Download it 

### 1.  Download **Beaver-Script.tar.xz**

### 2. Go to Downloads
```bash
cd ~/Downloads
```
```bash
ls
```

### 3. Extract the file
```bash
tar -xf Beaver.tar.xz
```
### 4. cd to folder 
```bash
cd Beaver
chmod +x Beaver.py
cd ..
```
###
### 5. Move the Beaver folder to any location you want, either manually or using 
```bash
sudo mv Beaver /path/you/want
``` 
### 6. Go to the Beaver folder and copy the new path of folder 

### 7. open terminal and add a command 
```bash
nano ~/.bashrc 
```
### 8. Scroll to the bottom of the file and add
```bash
alias Beaver='cd /New/path/of/beaver/folder && python3 Beaver.py'
```
### 9. Save it and exit
In nano, save the file by pressing CTRL + O, then Enter to confirm. Exit by pressing CTRL + X.
### 10. Apply the changes
```bash
source ~/.bashrc
```
### Now you can run it using the command
```bash
Beaver
```
