from xml.dom import minidom

drzewko = minidom.parse('plik.xml')
#print(drzewko.toxml())

nodes = drzewko.childNodes
#print(nodes[0].getElementsByTagName("osoba")[0].toxml())

for i in nodes[0].getElementsByTagName("osoba"):
    print(i.getElementsByTagName("imie")[0].nodeName)
    print(i.getElementsByTagName("imie")[0].childNodes[0].toxml())
    print(i.getElementsByTagName("imie")[0].getAttribute("aaa"))
