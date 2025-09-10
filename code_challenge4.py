print ("Good day, Welcome to the Manga Recommendation Center")
x = input ("Are you interested ? yes/no ") 

if ( x == "yes" ) or ( x == "YES" ) or ( x == "Yes" ) :
	anime = input ("What genre do you seem to be interested with : Comedy/Action/Horror \n ") .lower()
	decade = input ("What decades range of manga do you want to read : 1 (1990s) , 2 (2000s) \n ") .lower()
	L = input ("How long do you want to read a kind of manga: 1 ( long ) , 2 (short) \n ") .lower()
else:
	print("Okay thank you, come back if you're interested in reading some manga again")

if (anime == "Comedy") and (decade == '1') and (L == '1') :
	print ("I would highly recommend this to you ("Great Teacher Onizuka (GTO)") ")
elif (anime == "Comedy") and (decade == '2') and (L == '2') :
	print ("I would highly recommend this to you ("Yakitate Japan") ")
elif (anime == "Action") and (decade == '1') and (L == '1') :
	print ("I would highly recommend this to you ("Hunter X Hunter") ")
elif (anime == "Action") and (decade == '2') and (L == '2') : 
	print ("I would highly recommend this to you ("Death Note") ")
elif (anime == "Horror") and (decade == '1') and (L == '1') :
	print ("I would highly recommend this to you ("Berserk") ")
elif (anime == "Horror") and (decade == '2') and (L == '2') :
	print ("I would highly recommend this to you ("Tokyo Ghoul") ")
else :
	print ("Sorry, I don't have other type of genre that I could recommend to you, SORRY! ")
