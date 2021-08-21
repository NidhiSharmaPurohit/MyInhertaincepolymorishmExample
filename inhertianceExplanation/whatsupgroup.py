class whatsUpGroup:
    def __init__(self,groupName):
            self.groupname=groupName
            self.listofwhatsup=[]

    def add(self,whatsupmem):
        self.listofwhatsup.append(whatsupmem)

    def delete(self,whatsupmem):
        self.listofwhatsup.remove(whatsupmem)

    def send_message(self,message):
        for i in self.listofwhatsup:
            i.received_message(message)