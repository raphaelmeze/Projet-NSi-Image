# Projet-NSi-Image
Ceci est un projet de traitement d'images avec python réalisé en groupe de trois

J'ai créé les fonctions contours et mosaique je vous laisse faire les votres mais regardez ce que j'ai fait pour comprendre comment marche la bibliothèque
image = Image.open('poisson.jpg')

from PIL import Image

from random import shuffle

image = Image.open('poisson.jpg')

def niveaux_de_gris(image): 
    for x in range (image.width): 
        for y in range (image.height): 
            rouge=image.getpixel((x,y))[0] 
            bleu=image.getpixel((x,y))[1] 
            vert=image.getpixel((x,y))[2] 
            m=(rouge+bleu+vert)//3 
            image.putpixel((x,y),(m,m,m)) 
    image.show() 

def contours(image,seuil): 
    niveaux_de_gris(image) 
    for x in range (image.width): 
        for y in range (image.height): 
            if x==0: 
                couleur1=image.getpixel((x,y))[0] 
                couleur2=image.getpixel((x+1,y))[0] 
                difference=couleur1-couleur2 
                if difference>seuil: 
                    image.putpixel((x,y),(255,255,255)) 
                else: 
                    image.putpixel((x,y),(0,0,0)) 
            else: 
                couleur1=image.getpixel((x,y))[0] 
                couleur2=image.getpixel((x-1,y))[0] 
                difference=couleur1-couleur2 
                if difference>seuil: 
                    image.putpixel((x,y),(255,255,255)) 
                else: 
                    image.putpixel((x,y),(0,0,0)) 
    image.show()

def mosaique(image):
    mosaique=[]
    largeur, longueur = image.width, image.height
    for i in range (16):
        mosaique+=[image.crop(((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))]
    shuffle(mosaique)
    for i in range(16):
        image.paste(mosaique[i],((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))
    image.show()

def negatif(image):
    for x in range (image.width): 
        for y in range (image.height): 
            r, v, b=image.getpixel((x,y))
            image.putpixel((x,y),(255-r,255-v,255-b)) 
    image.show() 
def premier_plan (image):
    largeur, longueur = image.width, image.height
    for x in range (image.width): 
        for y in range (image.height): 
            if not((x>largeur//3 and x<largeur*2//3) and (y>longueur//3 and y<longueur*2//3)):
                rouge=image.getpixel((x,y))[0] 
                bleu=image.getpixel((x,y))[1] 
                vert=image.getpixel((x,y))[2] 
                m=(rouge+bleu+vert)//3 
                image.putpixel((x,y),(m,m,m))
    image.show()
