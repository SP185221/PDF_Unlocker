import pikepdf

file = '/Users/ADMIN/Desktop/test.pdf'  # wite the path of file you want to get the password

for i in range ( 1000, 2222,1):  #  Guess Logic 
    try:
        with pikepdf.open(file, password = str(i)) as pdf:
            num_pages = len(pdf.pages)
            print("\nCongratulations !!!  Password Cracked !!!")
            print("Total pages:", num_pages)
            print("Correct password", i)
            break
                
    except pikepdf._qpdf.PasswordError:
        print("invalid password", i )    
    
print("End of Program")
    
