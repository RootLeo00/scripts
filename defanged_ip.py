import re
def Defanged_IP(Str):
	x=re.sub("[.]","[.]",Str)
	print(x)
Str="1.1.1.2"
Defanged_IP(Str)
S = "255.100.50.0"
Defanged_IP(S)

#This code is contributed by pranjalpkp

