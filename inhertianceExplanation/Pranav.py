
from  whatsupmember import whatsUpMember

class Pranav(whatsUpMember):

    def received_message(self,message):
        print("Hi I am from Pranav " + str(message))