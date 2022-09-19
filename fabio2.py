
final_arquivo = False
string_vazia = ''
ips=[]
ips2=[]
ips3=[]
ips4=[]

ips_inv=[]
ips_inv2=[]
ips_inv3=[]
ips_inv4=[]



meu_arquivo = open('ips.txt', 'r')

while not final_arquivo:
    linha = meu_arquivo.readline().rstrip()    
    if linha == string_vazia:
        final_arquivo = True        
    else:
        info_ex2 = linha.split('.')
        ip1 = info_ex2[0]
        ip2 = info_ex2[1]
        ip3 = info_ex2[2]
        ip4 = info_ex2[3]
        if int(ip1) < 1 or int(ip1) > 255:
            ips_inv.append(ip1)
            ips_inv2.append(ip2)
            ips_inv3.append(ip3)
            ips_inv4.append(ip4)
        elif int(ip2)<0 or int(ip2) >255:
            ips_inv.append(ip1)
            ips_inv2.append(ip2)
            ips_inv3.append(ip3)
            ips_inv4.append(ip4)
        elif int(ip3)<0 or int(ip3) >255:
            ips_inv.append(ip1)
            ips_inv2.append(ip2)
            ips_inv3.append(ip3)
            ips_inv4.append(ip4)
        elif int(ip4)<0 or int(ip4) >255:
            ips_inv.append(ip1)
            ips_inv2.append(ip2)
            ips_inv3.append(ip3)
            ips_inv4.append(ip4)
        else:
            ips.append(ip1)
            ips2.append(ip2)
            ips3.append(ip3)
            ips4.append(ip4)

meu_arquivo.close()


invalido = open('ips_inv.txt', 'w')
for i in range(len(ips_inv)):
    invalido.write(ips_inv[i]+"."+ips_inv2[i]+"."+ips_inv3[i]+"."+ips_inv4[i]+'\n')

invalido.close()

valido = open('ipsV.txt', 'w')
for i in range(len(ips)):
    valido.write(ips[i]+"."+ips2[i]+"."+ips3[i]+"."+ips4[i]+'\n')

valido.close()






