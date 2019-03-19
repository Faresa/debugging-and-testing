import morse_utils

code = {'a':".-",'b':"-...",'c':"-.-.",'d' :"-..",'e':"." ,'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}

def code_for(letter) :
    #k = letter.lower
    return code[letter.lower()]

def transmit_letter(letter) :
    #p_string = ""
    #for x in range (len(letter)) :
    #    p_string =
    count = 0 
    for c in code_for(letter) :   
        count +=1
        #for i in range(len(code_for(letter))):
        if c == "-" :
            print(c,end="") 
            morse_utils.beep(500,500)
            #print("^",end ='') 
    
        if c == "." :
            morse_utils.sleep(1)
            print(".",end='')
            morse_utils.beep(1000,100)
                
        if count < len(code_for(letter)) :       
            print("^",end ='')
            #while i != (len(c)-1) :
        #if c != :code_for(letter)[-1] :
                #Sbreak
        
def transmit_word(word) :
    for i in word :
        transmit_letter(i)
        print('|',end='')
        
def word_pause() :
    print("||",end="")
    morse_utils.sleep(.7)

            
#def main():
 #   message = input("Enter your Message : \n").split(' ')    
  #  for e in message :
   #     transmit_word(e)
    #    word_pause()
    #print('')
    #code_for(letter)
    #transmit_letter(letter)
    
#main()