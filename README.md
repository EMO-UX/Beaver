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
tar -xf Beaver-Script.tar.xz
```
### 4. Move the Beaver folder to any location you want, either manually or using 
```bash
sudo mv Beaver /path/you/want
``` 
### 5. Go to the Beaver folder and open a terminal .

### 6. copy Beaver.py file to /home/your_username/.local/bin 
```bash
sudo cp Beaver.py /home/your_username/.local/bin
```

### Now you can run it using the command
```bash
Beaver.py
```
