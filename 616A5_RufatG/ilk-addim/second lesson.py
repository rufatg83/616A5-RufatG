class DuymeNode:
    def __init__(self, xana1, xana2):
        self.xana1 = xana1  
        self.xana2 = xana2  
        self.next = None
duyme1 = DuymeNode("A1", "A1")
duyme2 = DuymeNode("A2", "A2")
duyme3 = DuymeNode("A3", "A3")
duyme4 = DuymeNode("A4", "A4")
duyme5 = DuymeNode("A5", "A5")
duyme1.next = duyme2
duyme2.next = duyme3
duyme3.next = duyme4
duyme4.next = duyme5
cari_duyme = duyme1
index = 1
while cari_duyme is not None:
    print(f"{index}-ci Düymə -> Xana 1: {cari_duyme.xana1} | Xana 2: {cari_duyme.xana2}")
    cari_duyme = cari_duyme.next
    index += 1