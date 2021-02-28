#created by SimShelby

import json

class AnonymousSurvey:
    def __init__(self,question,response = [],newresponse = ''): #dont change the  default value
        self.question = question       
        self.response = response    #if this is  your first time you run this code 
                                       #dont add a response values or this code he wont run
                                           #becouse you need a list to store your data in json file
                                        
        

    def show_question(self):   #this methode he will print your question
        '''print question'''

        print(self.question)


    def store_response(self,newresponse): #this methode she will store all responses in json file
                                               #and u will return self.resposne 

        self.newresponse = newresponse
        file11 = 'responses.json'

        try:

            with open(file11) as f:
                self.response = json.load(f)
        except:
            with open(file11,'w') as f:

                json.dump(self.response,f)

            with open(file11) as f:
                self.response = json.load(f)

            with open(file11,'w') as f:    
                a = self.response
                a.append(self.newresponse)
                json.dump(a,f)

            return self.response
            
        else:
            with open(file11) as f:
                self.response = json.load(f)

                
            with open(file11,'w') as f:
                
                a = self.response
                a.append(self.newresponse)
                json.dump(a,f)


            self.response = a 
            return self.response

    def show_all_respones(self):    #this methode she will return all answers in the json file"
        file11 = 'responses.json'
        with open(file11) as f:  
            a = json.load(f)  
        print('the result for your last survey is')

        for i in a:
            print(f'* {i}')
