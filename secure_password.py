# geektechstuff
# How secure is the password?

def ask_for_password():
    password = input("Please type password: ")
    print("You typed",password)
    return(password)

def check_basics(password):
    # alphabets, number and special characters
    uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    special = ["!","@","£","%","^","&","*","~"]
    # counts
    upper_count = 0
    lower_count = 0
    number_count = 0
    special_count = 0
    counts_total = 0
    uc = 0
    lc = 0
    nc = 0
    sc = 0
    p_length = 0
    detectpwned = 0
    # start scoring
    print("Password complexity:")
    for x in password:
        for y in uppercase:
            if x == y:
                upper_count = upper_count+1
                uc= 1
        for z in lowercase:
            if x == z:
                lower_count = lower_count+1
                lc = 1
        for w in numbers:
            if x == w:
                number_count = number_count+1
                nc = 1     
        for v in special:
            if x == v:
                special_count = special_count+1
                sc = 1            
    if uc == 1:
        print("Password contains an upper case character")
    if lc == 1:  
        print("Password contains a lower case character")
    if nc == 1:   
        print("Password contains a number")    
    if sc == 1:
        print("Password contains a special character")

    print("Current NCSC guidence is not to use complexity requirements: https://www.ncsc.gov.uk/collection/passwords/updating-your-approach")
    # check password length
    print("Password length check: ")
    p_length = len(password)
    if p_length > 8:
        print("Password is greater than 8 characters.")
        print("NCSC recommend not having a short password: https://www.ncsc.gov.uk/collection/passwords/updating-your-approach")
    else:
        print("NCSC recommened not having a short password: https://www.ncsc.gov.uk/collection/passwords/updating-your-approach")

    # check pwned passwords
    f = open("PwnedPasswordTop100k.txt","r")
    for x in f:
        x = str(x)
        x = x.strip()
        if x == password:
            print("Password is in top 100,000 pwned passwords")
            detectpwned = 1
    if detectpwned == 0:
            print("Password not detected in top 100,000 pwned passwords")
    print("The list of top 100,000 pwned passwords available at: https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordTop100k.txt")
    print("Read more on the top pwned passwords at: https://www.ncsc.gov.uk/blog-post/passwords-passwords-everywhere")
    return()

check_basics("georgeisadick")