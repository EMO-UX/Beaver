import csv
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
folder_path = "data"
savefile = "data/savefile.csv"

console.print(Panel("", title="[bold blue]Beaver[/bold blue]",title_align="center", expand=True, border_style="Blue", padding=(1, 40)))
os.makedirs(folder_path,exist_ok=True)
 
# التحقق من وجود الملف، وإذا لم يكن موجودًا يتم إنشاؤه
if not os.path.exists("data/savefile.csv"):
    with open(("data/savefile.csv"),'w+'):
        pass
 # إدخال البيانات من المستخدم
def input_function():
   row1 = input(" Username: ")
   row2 = input(" Secure Password: ")
   row3 = input(" Service Name: ")
   row4 = input(" Recovery Email/Phone: ")
   return [row1, row2, row3, row4]

# إضافة البيانات إلى الملف
def add_function(ithems):
    with open ("data/savefile.csv",'a',newline='') as write_savefile:
        writer = csv.writer(write_savefile)
        writer.writerow(ithems)

# قراءة وعرض محتويات الملف
def read_function():
    table = Table(title="Saved Data", title_style="bold blue",border_style="#b3e5fc",header_style="bold #1E3A8A")
    table.add_column("Username",justify="left")   
    table.add_column("Secure Password",justify="left")         
    table.add_column("Service Name",justify="left")
    table.add_column("Recovery Email/phone",justify="left")
    with open(savefile,'r',newline='') as read_savefile:
        reader = csv.reader(read_savefile)
        lines = list(reader)
        if lines:
            for line in lines:
                table.add_row(*line)
            console.print(table)
        else:
            console.print("[bold yellow]No data found in the CSV file![/bold yellow]")
# حذف سطر معين بناءً على رقم السطر
def delete_function():
    try:
        delete_Number = int(input("Enter the number of the line you want to delete it :"))
        with open("data/savefile.csv",'r',newline='') as delete_file:
            lines = list(csv.reader(delete_file))
            if 0<= delete_Number <= len(lines):
                del lines[delete_Number - 1]
                console.print("[bold green]Deleted successfully[/bold green]")
                with open("data/savefile.csv",'w',newline='') as newfile:        
                    writer = csv.writer(newfile)
                    writer.writerows(lines)
            else:
                console.print("[bold red]Number of line is uncorect [/bold red]")
    except ValueError:
        console.print("[bold yellow]Please enter a valid number.[/bold yellow]")

#add_function(ithems)
#read_function()
#delete_fuction()
while True:
    c_input = input("\nOptions: Read, Add, Delete, or Exit : ").lower().replace(" ","")
    print("")
    if c_input == ("add"):
        ithems = input_function()
        add_function(ithems)
    elif c_input == ("read"):
        read_function()
    elif c_input== ("delete"):
        delete_function()
    elif c_input == ("exit"):
        break
    else:
        print("[bold yellow] This command does not exist. Please try again! [/bold yellow]")
