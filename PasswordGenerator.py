import random

length = int(input("How long should the password be: "))
lowercase = "qwertyuiopåsdfghjklöäzxcvbnm"
uppercase = "QWERTYUIOPÅASDFGHJKLÖÄZXCVBNM"
numbers   = "123456789"
specials  = "!#¤%&/()=?@£$€¥{[]}"
all = lowercase + uppercase + numbers + specials

password = "".join(random.sample(all, length))
print(password)
 
