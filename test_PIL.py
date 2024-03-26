https://boulevard-des-fleurs.fr/469-large_default/rose-rouge.jpg

from PIL import Image

from random import shuffle

image = Image.open('poisson.jpg')

def niveaux_de_gris(image): 
    img2=image.copy()
    for x in range (img2.width): 
        for y in range (img2.height): 
            rouge=img2.getpixel((x,y))[0] 
            bleu=img2.getpixel((x,y))[1] 
            vert=img2.getpixel((x,y))[2] 
            m=(rouge+bleu+vert)//3 
            img2.putpixel((x,y),(m,m,m)) 
    return img2 

def contours(image,seuil):
    img2=image.copy()
    niveaux_de_gris(img2)
    for x in range (img2.width-1): 
        for y in range (img2.height): 
            if x==0: 
                couleur1=img2.getpixel((x,y))[0] 
                couleur2=img2.getpixel((x+1,y))[0] 
                difference=abs(couleur1-couleur2)
                if difference>seuil: 
                    img2.putpixel((x,y),(255,255,255)) 
                else: 
                    img2.putpixel((x,y),(0,0,0))
            else: 
                couleur1=image.getpixel((x,y))[0] 
                couleur2=image.getpixel((x+1,y))[0] 
                difference=abs(couleur1-couleur2)
                if difference>seuil: 
                    img2.putpixel((x,y),(255,255,255)) 
                else: 
                    img2.putpixel((x,y),(0,0,0)) 
    return img2

def mosaique(image):
    mosaique=[]
    img2=image.copy()
    largeur, longueur = image.width, image.height
    for i in range (16):
        mosaique+=[img2.crop(((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))]
    shuffle(mosaique)
    for i in range(16):
        image.paste(mosaique[i],((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))
    image.show()

def noir_et_blanc(image,seuil):
    image_nb=image.copy()
    for x in range (image_nb.width):
        for y in range(image_nb.height):
            rouge=image_nb.getpixel((x,y))[0]
            bleu=image_nb.getpixel((x,y))[1] 
            vert=image_nb.getpixel((x,y))[2] 
            moyenne=(rouge+bleu+vert)//3
            if moyenne > seuil:
                image_nb.putpixel((x,y),(255,255,255))
            else:
                image_nb.putpixel((x,y),(0,0,0))
    image_nb.show()

def negatif(image):
    """negatif
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    None.
"""
    img2=image.copy()
    for x in range (img2.width): 
    #ça regarde la largeur de l'image
        for y in range (img2.height): 
        #ça regarde la longueur de l'image
            r, v, b=img2.getpixel((x,y))
            #ça prend toutes les couleurs de tous les pixels de l'image
            img2.putpixel((x,y),(255-r,255-v,255-b)) 
            #ça remplace les pixels par leur pixels négatifs en rajoutant 255 à chaque couleur de chaque pixel
    return img2
    #ça retourne l'image modifiée

def premier_plan (image,):
    img2=image.copy()
    r=int(input("Quelle valeur de rouge voulez-vous gardez ?"))
    b=int(input("Quelle valeur de bleu voulez-vous gardez ?"))
    v=int(input("Quelle valeur de vert voulez-vous gardez ?"))
    tolerance=int(input("Quelle tolérance acceptez-vous autour de cette couleur ?"))
    for x in range (img2.width): 
        for y in range (img2.height): 
            rouge=img2.getpixel((x,y))[0] 
            vert=img2.getpixel((x,y))[1]
            bleu=img2.getpixel((x,y))[2]
            if not((rouge>r-tolerance and rouge<r+tolerance)and(bleu>b-tolerance and bleu<b+tolerance)and(vert>v-tolerance and vert<v+tolerance)):
                m=(rouge+bleu+vert)//3
                img2.putpixel((x,y),(m,m,m))
    return img2
