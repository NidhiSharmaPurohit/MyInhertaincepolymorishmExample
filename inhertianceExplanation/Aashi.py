from  whatsupmember import whatsUpMember


class Aashi(whatsUpMember):

    def received_message(self, message):
        print("Hi I am from Aashi  " + str(message))
