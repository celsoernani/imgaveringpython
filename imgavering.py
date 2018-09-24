from PIL import Image, ImageFilter
import numpy as np
import cv2

#Read image
##im = Image.open( 'leao.png' )
##img = Image.open( 'leao.png' ).convert('LA')
##img.save('greyscale.png')
##im.show()
##img.show()


def newimage(img, arraynew, size):
    aux = 0
    for i in range(0,size-1):
        for j in range(0,size-1):
            img[i, j] = int(arraynew[aux])
            aux = aux + 1
    return img


def imgavering(matrix, tamanho, passo):
     q = 0
     p = 2
     n = 0
     k = 2
     a = 0
     b = 0
     temp2 = tamanho - passo
     temp3 = tamanho - 2
     temp4 = tamanho - 2
     soma = 0
     result = []
     while(((n <= temp2) and (k <= temp3)) and ((q <= temp2) and (p <= temp3))):
         for i in range(n, k+1):
             for j in range(q, p+1):
                 soma = matrix[i, j] + soma
         q = q+1
         p = p + 1
         aux = soma/(pow(passo, 2))
         result.append(aux)
         aux = 0
         soma = 0
         b = b+1
         if(b == temp4):
             b = 0
             a = a+1
         if ((q == temp4 - 1) and (p == tamanho - 1)):
            p = 2
            q = 0
            n = n+1
            k = k+1
     return (result)

     
##TO OPENCV
img = cv2.imread('leao.png')
height, width, rgb = img.shape
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Imagem em tons de cinza: ")
print(gray_image)

size = height # or width, imagem tem que ser quadrada
newsize = (size - 2)
sizes = (newsize -1, newsize-1)
matriznewimg = np.zeros(sizes)
print(matriznewimg)
newimagarray = imgavering(gray_image, size, 3)
newimagem = newimage(matriznewimg, newimagarray, newsize)
print("Imagem reduzida em tons de cinza: ")
print(newimagem)

cv2.imshow('leao.png', img)
cv2.imwrite('gray_image.png', gray_image)
cv2.imwrite('imgred.png', newimagem)
cv2.imshow('gray_image', gray_image)
cv2.imshow('imgred.png', gray_image)
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
