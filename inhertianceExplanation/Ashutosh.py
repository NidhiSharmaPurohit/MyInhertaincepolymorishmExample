from  whatsupmember import whatsUpMember


class Ashutosh(whatsUpMember):

    def received_message(self, message):
        print("Hi I am from Ashutosh  " + str(message))
