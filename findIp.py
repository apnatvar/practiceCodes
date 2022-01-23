import ipcalc
print ("Format for ipv4 address: x.x.x.x/x")
print ("Format for ipv6 address: x:x:x:x:x:x/x")
ipAddress = input("Enter the ip address: ")
possibleCombinations = 0
for _ in ipcalc.Network(ipAddress):
   possibleCombinations = possibleCombinations + 1
subnet = ipcalc.Network(ipAddress)
print ("-----------------------------")
print ("Possible Combo: " + str(possibleCombinations))
print ("Subnet Mask: " + str(subnet.netmask()))
if subnet.netmask() == "255.0.0.0":
    print ("Class A")
elif subnet.netmask() == "255.255.0.0":
    print ("Class B")
elif subnet.netmask() == "255.255.255.0":
    print ("Class C")
elif subnet.netmask() == "255.255.255.252":
    print ("Class D")
print ("-----------------------------")
