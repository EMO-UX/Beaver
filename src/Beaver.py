import csv
import os


savefile = "savefile.csv"
# التحقق من وجود الملف، وإذا لم يكن موجودًا يتم إنشاؤه
if not os.path.exists(savefile):
    with open(("savefile.csv"),'w+'):
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
    with open ("savefile.csv",'a',newline='') as write_savefile:
        writer = csv.writer(write_savefile)
        writer.writerow(ithems)

# قراءة وعرض محتويات الملف
def read_function():
    count = 1
    with open("savefile.csv",'r',newline='') as read_savefile:
        reader = csv.reader(read_savefile)
        for line in reader:
            print(f"{count} - {(' / ').join(line)} ")
            count += 1            

# حذف سطر معين بناءً على رقم السطر
def delete_function():
    try:
        delete_Number = int(input("Enter the number of the line you want to delete it :"))
        with open("savefile.csv",'r',newline='') as delete_file:
            lines = list(csv.reader(delete_file))
            if 0<= delete_Number <= len(lines):
                del lines[delete_Number - 1]
                print("Deleted successfully")
                with open("savefile.csv",'w',newline='') as newfile:        
                    writer = csv.writer(newfile)
                    writer.writerows(lines)
            else:
                print("Number of line is uncorect ")
    except ValueError:
        print("Please enter a valid number.")

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
        print("This command does not exist. Please try again!")







