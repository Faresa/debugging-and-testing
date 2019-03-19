# Tech Support
# Stephan Jamieson
# 5/1/2015
responses={
    'bluetooth':'Have you tried mouthwash?',
    'windows':'Ah, I think I see your problem. What version?',
    'apple':'You do mean the computer kind?',
    'blue':'Ah, the blue screen of death. And then what happened?',
    'spam':'You should see if your mail client can filter messages.',
    'connection':'Contact Telkom.',
    'crashed':'Are the drivers up to date?',
    'hacked':'You should consider installing anti-virus software.'}

def default_response():
    return 'Curious, tell me more.'

def print_welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')

def get_input():
    query = input("").split()
    #print("Query :",query)
    return query

def get_response(x) :
    for word in x:
        word = word.lower()
        if word== "quit" : return
        if word in responses :
           # print("Word = ",word)
            #print (responses[word.lower()])
            return responses[word]
        
        #else : pass
    return default_response()
        
        
        #print(word)
        
   # if word.lower()!= "quit" and word.lower() not in responses : 
            
        
        


def main():
    print_welcome()
    query = get_input()
    #quit = query
    get_response(query)
    while True :
        if query[0].lower() == 'quit' : break    
        else :
            print(get_response(query))
            query=get_input()
        
main()
    