# if the given string S1 = "Maha Bharat", generate the following strings by manipulate S1

# "Bharat"
# "mAHA bHARAT"
# "BharatBharatBharat"
# "Mera Bharat"
# "Mera Bharat Mahan"

S = "Maha Bharat"

S1 = S[-6:]
print(S1)
S3 = S1*3
print(S3)
S4 = "Mera " + S1
print(S4)
S5 = S4 + " Mahan"
print(S5)
S2 = S.swapcase()
print(S2)
