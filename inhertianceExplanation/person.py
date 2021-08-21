from Nidhi import *
from Ashutosh import *
from Pranav import *
from Aashi import *
from whatsupgroup import *

A1 = Ashutosh()
Aa1 = Aashi()
P1 = Pranav()


group1=whatsUpGroup("purohit")
group1.add(A1)
group1.add(Aa1)
group1.add(P1)

group1.send_message("Hello ")


N1=Nidhi()
group1.add(N1)
group1.delete(A1)
group1.send_message("bye hero")





