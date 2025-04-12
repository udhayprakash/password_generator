import secrets

alphabet = "abcdefghijklmnopqrstuvwxyz .,!@_-(*)-+/|$%&=?^"
pw_length = 37 #can change the length of your password by changing this number
mypw = ""

for i in range(pw_length):
    next_index = secrets.SystemRandom().randrange(len(alphabet))
    mypw = mypw + alphabet[next_index]

# replace 2 characters with a number, if you wish to replace more characters increase "for i in range(random.randrange(1,[THIS NUMBER]))"
for i in range(secrets.SystemRandom().randrange(1,4)):
    replace_index = secrets.SystemRandom().randrange(len(mypw)//2)
    mypw = mypw[0:replace_index] + str(secrets.SystemRandom().randrange(10)) + mypw[replace_index+1:]

# replace 2 characters with a number, if you wish to replace more characters increase "for i in range(random.randrange(1,[THIS NUMBER]))"
for i in range(secrets.SystemRandom().randrange(1,4)):
    replace_index = secrets.SystemRandom().randrange(len(mypw)//2,len(mypw))
    mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]

print(mypw)
