'''
Author : Imanpalsingh <imanpalsingh@gmail.com>
Date created : 26-02-21

'''


from PIL import Image
import numpy as np


def strToBin(message):
    '''
    Function to convert a string representing ascii characters to a string representing binary equivalent

    params
    @message : The ascii string to convert
    @return : binary quivalent string
    '''
    return ''.join([bin(ord(x))[2:].zfill(8) for x in message])



def binToStr(message):

    '''
    Function to convert a string representing binary equivalent of an ascii to a string representing the 
    actual ascii

    params
    @message : binary string
    @return : The ascii string equivalent
    '''
    
    return ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)//8))



def encode(image, message):
    

    '''
    Function encode the message inside the picture

    For each pixel having three values of R G B, the function assigns the bits of the 
    message to the least signification bits of R G B of each pixel until the message is
    encoded completely.

    params
    @image : A PIL (pillow loaded) Image 
    @message : string to encode in the image
    @return : The encode image and length of the bits inserted (for easier decoding)
    '''

    imgMat = np.array(image)

    msgBin = strToBin(message)
    msgIndex  = 0 

    for row in range(len(imgMat)):

        for col in range(len(imgMat[row])):

            pixVal = imgMat[row][col]

            for color in range(0,3):

                if(msgIndex < len(msgBin)):

                    pixVal[color] = (pixVal[color] & ~1) | (int(msgBin[msgIndex]))
                    msgIndex+=1

    return Image.fromarray(imgMat), len(msgBin)


def decode(image, msgLen):

    '''
    Function to decode the message from the encoded image

    For each pixel having three values of R G B, the function reads the bits of the 
    message to the least signification bits of R G B of each pixel until the specified number of modifications are reached.
    It then converts the binary string read so far to ascii equivalent

    params
    @image : A PIL (pillow loaded) Image (already encoded)
    @msgLen : the number of LSBs modified during encoding (can be approximated)
            If the value passed is lesser than what its supposed to be : The origianl plaintext might be truncated
            If the value passed is greater than what its supposed to be : Random ascii noise will be 
            appended to the origianl plaintext. 
    @return : The decoded message
    '''

    imgMat = np.array(image)
    msgIndex = 0
    message=""


    for i in range(len(imgMat)):

        for j in range(len(imgMat[i])):

            pixVal = imgMat[i][j]

            for color in range(0,3):

                    if(msgIndex < msgLen):

                        message+=str(pixVal[color] & 1)
                        msgIndex+=1

    return binToStr(message)

