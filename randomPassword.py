import string
import random
password  = ''.join([random.choice(string.ascii_lowercase+string.digits+string.ascii_uppercase
                                   +str('@')+ str('%')+str('!')+str('&')
                                   ) for i in range(7)])
print password
