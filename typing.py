#Company Scenario
#The company AOL is sold to a company called Snores, we have to replace the domain of emails listed as AOL and change it to Snores
#live.com is now broadcast.com
a = open("typing.txt","r")
b = a.readlines()
c=str(b)
emails=c.split()
new_domain = "snores.com"
old_domain = "aol.com"
new_domain2 = "broadcast.com"
old_domain2 = "live.com"
def replace(email,new_domain,old_domain,new_domain2,old_domain2):
    if "@"+old_domain in email:
        index  = email.index("@"+old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    elif "@"+old_domain2 in email:
        index  = email.index("@"+old_domain2)
        new_email2 = email[:index] + "@" + new_domain2
        return new_email2
    return email
for email in emails:
    print(replace(email,new_domain,old_domain,new_domain2,old_domain2))
