email = 'test@domain.com'
#input("What is your E-Mail? ") 
print(email)
name = email.split('@')[0]
domain = (email.split('@')[1]).split('.')[0]
print(email)
print("Username: {0}, domain: {1}".format(name, domain))
