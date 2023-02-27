# String
myStr = "thisisit"

# Looping
while myStr != "":
	slen0 = len(myStr)
	ch = myStr[0]
	myStr = myStr.replace(ch, "")
	slen1 = len(myStr)
	if slen1 == slen0-1:
		print ("First non-repeating character = ",ch)
		break;
	else:
		print ("No Unique Character Found!")