'''
Created on 2 mars 2018

@author: M.Dien
'''
'''
Created on 19 avr. 2016
@author: menez

Attention ce code est une horreur :-)
Il n'a qu'une vertu vous montrer comment analyser 
les enregistrements trames Ethernet .

N'oubliez qu'il y a un aspect "art" dans la programmation
et qu'au dela du resultat fonctionnel, la structure compte 
tout autant !!
'''

import socket
from struct import *
import binascii

#====================================================

def manipulation_binascii():
    """
    Jouons "juste ce qu'il faut" avec les octets ...
    """
    
    """ La fonction ord() """
    c = 'A'
    print(type(c)) # 'str' en python
    v = ord(c) # code ascii de c = i.e representation numerique de c
    print("c={} est code par {} = 0x{:x}".format(c,v,v))
    
    """  Definition classique d'une string  """
    s = "ff00" # une string representant un hexadecimal
    print(type(s))
    print(s)

    # s[i] vaut le code ascii d'un caractere */
    print(type(s[1])) # 'str' en python

    print ("Caracteres de la chaine : {} / {} / {} / {}".format(s[0], s[1] , s[2], s[3]))
    print ("Code Ascii de la chaine : {:x} / {:x} / {:x} / {:x}".format(ord(s[0]), ord(s[1]) , ord(s[2]), ord(s[3])))

    """ supposons que s represente une valeur hexa  : on voudrait recuperer cette valeur """ 
    # => on va obtenir de 2 octets (on rappelle qu'un octet c'est deux chiffres hexa).
    # => donc on voudrait former deux octets [FF] et [00]
    
    ba = binascii.unhexlify(s)
    # Return the binary data represented by the hexadecimal string hexstr
    print(type(ba))    # ba est une string d'octet => bytes object !
    print ("ba  = {}".format(ba))
    print ("len(ba)  = {}".format(len(ba)))  
    print(type(ba[1])) # ba[1] est un octet ... type comme un int
    print ("ba[0] = {:02x}".format(ba[0]))   # octet 0 ecrit en hexa
    print ("ba[1] = {:d}".format(ba[1]))     # octet 1 ecrit en decimal

    """ En sens inverse : de la valeur vers la string """    
    s = binascii.hexlify(ba)
    print(type(s))
    print("s : {}".format(s))
    
    ba = b'\xFF\x00' # ba est une string d'octets !
    print(type(ba))  # donc "bytes"
    print(ba) # ca affiche les caracteres de code ASCII 'FF' et '00'  
    s = binascii.hexlify(ba)
    print(type(s)) # s est une string de caracteres 
    print ("Caracteres de la chaine : {} / {} / {} / {}".format(s[0], s[1] , s[2], s[3]))

#====================================================

def readtrames(filename):
    """
    Cette fonction fabrique une liste de chaines de caracteres a partir du 
    fichier contenant les trames.
    
    Chaque chaine de la liste est une trame du fichier.
    
    return : liste des trames contenues dans le fichier
    """
    file = open(filename)
    trames = [] # List of frames (= trames)
    trame = ""  # Current frame
    i = 1
    for line in file : # acces au fichier ligne par ligne
        line = line.rstrip('\n') # on enleve le retour chariot de la ligne
        line = line[6:53]        # on ne garde que les colonnes interessantes  
        print ("l {} : {}".format(i,line))
        
        if (len(line) == 0): # Trame separator
            #print "Ligne vide :", (len(line))
            trame = trame.replace(' ','') # on enleve le blanc 
            trames.append(trame) # on ajoute la trame a la liste 
            trame = ""
        else :
            trame = trame + line #.rstrip(' ') + ' '
        
        i = i+1
    
    return trames

#====================================================

def decodageEthernet(trame):
    """
    Analyse une trame Ethernet :
    cf https://fr.wikipedia.org/wiki/Ethernet    
    Input : trame est une chaine de caracteres
    """
    print ("\n\nTrame Ethernet a analyser : \n\t{}\n".format(trame))
    trame = binascii.unhexlify(trame) # Les octets representes par cette chaine

    # Parse ethernet header
    print ("Header Ethernet :")       
    eth_length = 14 
    eth_header = trame[:eth_length]  # Get the bytes of the header 
    print (type(eth_header))
    
    # using Python slicing
    print ('Destination MAC : {}'.format(binascii.hexlify(eth_header[0:6])))
        
    # or using unpack
    # For more information on format strings and endiannes, refer to
    # https://docs.python.org/3.5/library/struct.html
    ethfields = unpack('!6s6sH' , eth_header) 
    adrd_mac = ethfields[0]
    print ('Destination MAC : {}'.format(binascii.hexlify(adrd_mac)))
    adrs_mac = ethfields[1]

    # Parse the payload : TODO
    # Get the bytes

#=================================================================

if __name__ == '__main__':
    
    #Pour comprendre les manipulations de bytes :
    manipulation_binascii()
    
    # Transformation des echanges contenus dans le fichier
    # vers une liste de strings  
    trames = readtrames("XXX.txt")
    print(trames)

    # Analyse de chaque trame de la liste
    for trame in trames:
        decodageEthernet(trame)        
