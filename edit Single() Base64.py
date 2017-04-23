import os
import binascii


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def Chose():
    print('\033[35m' + '   1) ' + '\033[32m' + 'Text To base64')
    print('\033[35m' + '   2) ' + '\033[32m' + 'File to base64')
    print('\033[35m' + '   3) ' + '\033[32m' + 'About, Help')
    print('\033[37m')

def Select_pr():
    print('\033[35m' + '   1) ' + '\033[32m' + 'base64 Encode')
    print('\033[35m' + '   2) ' + '\033[32m' + 'base64 Decode')
    print('\033[37m')

def ByeByE():
    print('\033[36m' + '   	BBBBBBBBBBBBBBBBB                                                   ')
    print('\033[36m' + '   	B::::::::::::::::B                                                  ')
    print('\033[36m' + '   	B::::::BBBBBB:::::B                                                 ')
    print('\033[36m' + '   	BB:::::B     B:::::B ' + '\033[37m' + ' Developer : ' + '\033[32m' + ' jok3r ')
    print('\033[36m' + '   	  B::::B     B:::::Byyyyyyy           yyyyyyy    eeeeeeeeeeee       ')
    print('\033[36m' + '   	  B::::B     B:::::B y:::::y         y:::::y   ee::::::::::::ee     ')
    print('\033[36m' + '   	  B::::BBBBBB:::::B   y:::::y       y:::::y   e::::::eeeee:::::ee   ')
    print('\033[36m' + '   	  B:::::::::::::BB     y:::::y     y:::::y   e::::::e     e:::::e   ')
    print('\033[36m' + '   	  B::::BBBBBB:::::B     y:::::y   y:::::y    e:::::::eeeee::::::e   ')
    print('\033[36m' + '   	  B::::B     B:::::B     y:::::y y:::::y     e:::::::::::::::::e    ')
    print('\033[36m' + '   	  B::::B     B:::::B      y:::::y:::::y      e::::::eeeeeeeeeee     ')
    print('\033[36m' + '   	  B::::B     B:::::B       y:::::::::y       e:::::::e              ')
    print('\033[36m' + '   	BB:::::BBBBBB::::::B        y:::::::y        e::::::::e             ')
    print('\033[36m' + '   	B:::::::::::::::::B          y:::::y          e::::::::eeeeeeee     ')
    print('\033[36m' + '   	B::::::::::::::::B          y:::::y            ee:::::::::::::e     ')
    print('\033[36m' + '   	BBBBBBBBBBBBBBBBB          y:::::y               eeeeeeeeeeeeee     ')
    print('\033[36m' + '   	                          y:::::y  ' + '\033[35m' + 'Iran-CyBeR.NeT ')
    print('\033[36m' + '   	                         y:::::y                                    ')
    print('\033[36m' + '   	                        y:::::y  ' + '\033[33m' + 'ByE bYe Brow :)  ')
    print('\033[36m' + '   	                       yyyyyyy                                      ')
    print('\033[37m')

def banner():
    print('\033[36m' + '   	IIIIIIIIII        CCCCCCCCCCCCC        GGGGGGGGGGGGG ')
    print('\033[36m' + '   	I::::::::I     CCC::::::::::::C     GGG::::::::::::G ')
    print('\033[36m' + '   	I::::::::I   CC:::::::::::::::C   GG:::::::::::::::G ')
    print('\033[36m' + '   	II::::::II  C:::::CCCCCCCC::::C  G:::::GGGGGGGG::::G ')
    print('\033[36m' + '   	I::::I   C:::::C       CCCCCC G:::::G       GGGGGG ')
    print('\033[36m' + '   	I::::I  C:::::C              G:::::G               ')
    print('\033[36m' + '   	I::::I  C:::::C              G:::::G               ')
    print('\033[36m' + '   	I::::I  C:::::C              G:::::G    GGGGGGGGGG ')
    print('\033[36m' + '   	I::::I  C:::::C              G:::::G    G::::::::G ')
    print('\033[36m' + '   	I::::I  C:::::C              G:::::G    GGGGG::::G ')
    print('\033[36m' + '   	I::::I  C:::::C              G:::::G        G::::G ')
    print('\033[36m' + '   	I::::I   C:::::C       CCCCCC G:::::G       G::::G ')
    print('\033[36m' + '   	II::::::II  C:::::CCCCCCCC::::C  G:::::GGGGGGGG::::G ')
    print('\033[36m' + '   	I::::::::I   CC:::::::::::::::C   GG:::::::::::::::G ')
    print('\033[36m' + '   	I::::::::I     CCC::::::::::::C     GGG::::::GGG:::G ')
    print('\033[33m' + '     	    IRAN-CybEr.NeT @ 2013 - 2017                 ')
    print('\033[32m' + '   	           Developer : jok3r                         ')
    print('\033[35m' + '   	          Telegram : Publish                         ')

    print('\033[37m')



cls()
banner()


def Help_options():
    cls()
    banner()
    print('\033[31m' + ' ------------------------------------------------------------  ')
    print('\033[36m' + ' This is Simple project For decode and Encode base64  ')
    print('\033[32m' + ' option 1 for Text to base64 ')
    print('\033[35m' + ' option 2 for file.txt to base64 ')
    print('\033[31m' + ' ------------------------------------------------------------  ')
    print('\033[37m')


def Multi():
    
    def base64_Decode():
        cls()
        banner()
        try:
            Encoded_File = raw_input("   Chose File : ")
            with open(Encoded_File, 'r') as x, open('decoded64.txt', 'w') as done:
                for line in x:
                    decoded_line = binascii.a2b_base64(line.strip())
                    done.write(decoded_line + "\n")
                    print('\033[35m' + "\n\n Decoded ! \n\n")
                    print('\033[32m' + " Result : " + '\033[31m' + decoded_line)
                    print('\033[37m')
        except:
            pass

    def base64_EnCode():
        cls()
        banner()
        try:
            Decoded_File = raw_input("   Chose File : ")
            with open(Decoded_File, 'r') as x, open('encoded64.txt', 'w') as done:
                for line in x:
                    encoded_line = binascii.b2a_base64(line.strip())
                    done.write(encoded_line + "\n")
                    print('\033[35m' + "\n\n Encoded ! \n\n")
                    print('\033[32m' + " Result : " + encoded_line)
                    print('\033[37m')
        except:
            pass
    cls()
    banner()
    Select_pr()
    Chose = raw_input(' Enter Your Method : ')
    if Chose == '1':
        base64_EnCode()
    if Chose == '2':
        base64_Decode()
    if Chose == '':
        cls()
        ByeByE()


def Single():

    def base64_Decode():
        cls()
        banner()
        try:
            Encoded_File = raw_input("   Enter your Text : ")
	    redecoded = raw_input("	Re Decode :  ")
            decoded_line = binascii.a2b_base64(Encoded_File.strip())
	    print('\033[35m' + "\n\n base64 Decoded ! \n\n")
	    print('\033[32m' + " Result : " + '\033[31m' + decoded_line)
	    print('\033[37m')
	    if (int(redecoded)>int(1)):
		    for x in range(int(1),int(redecoded)):
		    		decoded_line = binascii.a2b_base64(decoded_line.strip())
				print('\033[35m' + "\n\n base64 Decoded ! \n\n")
				print('\033[32m' + " Result : " + '\033[31m' + decoded_line)
				print('\033[37m')
	    
        except:
            
                        	pass

    def base64_EnCode():
        cls()
        banner()
        try:
            Decoded_File = raw_input("   Enter your Text : ")
	    redecoded = raw_input("	Re Encode :  ")
	    decoded_line = binascii.b2a_base64(Decoded_File.strip())
	    print('\033[35m' + "\n\n base64 Encoded ! \n\n")
	    print('\033[32m' + " Result : " + '\033[31m' + decoded_line)
	    print('\033[37m')
	    if (int(redecoded)>int(1)):
		    for x in range(int(1),int(redecoded)):
				decoded_line=binascii.b2a_base64(decoded_line.strip())
				print('\033[35m' + "\n\n base64 Encoded ! \n\n")
				print('\033[32m' + " Result : " + '\033[31m' + decoded_line)
				print('\033[37m')
	except:
	    			pass

    cls()
    banner()
    Select_pr()
    Chose = raw_input(' Enter Your Method : ')
    if Chose == '1':
        base64_EnCode()
    if Chose == '2':
        base64_Decode()
    if Chose == '':
        cls()
        ByeByE()


cls()
banner()
Chose()
Chose2 = raw_input(' Enter Your Method : ')
if Chose2 == '':
    cls()
    ByeByE()
if Chose2 == '1':
    Single()
if Chose2 == '2':
    Multi()
if Chose2 == '3':
    Help_options()
