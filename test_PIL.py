https://boulevard-des-fleurs.fr/469-large_default/rose-rouge.jpg

from PIL import Image

from random import shuffle

image = Image.open('poisson.jpg')

def niveaux_de_gris(image): 
    """niveaux_de_gris
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    None.
"""
    img2=image.copy()
    #ça copie l'image dans une variable img2
    for x in range (img2.width): 
    #ça regarde la largeur de l'image
        for y in range (img2.height): 
        #ça regarde la longueur de l'image
            rouge=img2.getpixel((x,y))[0] 
            #ça prend la valeur de la couleur rouge de chaque pixel et la met dans la variable rouge
            bleu=img2.getpixel((x,y))[1] 
            #ça prend la valeur de la couleur bleue de chaque pixel et la met dans la variable bleu
            vert=img2.getpixel((x,y))[2] 
            #ça prend la valeur de la couleur verte de chaque pixel et la met dans la variable vert
            m=(rouge+bleu+vert)//3 
            #ça fait la moyenne de toutes les couleurs de chaque pixel
            img2.putpixel((x,y),(m,m,m)) 
            #ça remplace les valeurs des couleurs des pixels par les valeurs des couleurs de la moyenne des pixels
    return img2 
    #ça montre l'image modifiée

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
    """mosaique
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    None.
"""
    mosaique=[]
    #ça définit la variable mosaique à un tableau vide
    img2=image.copy()
    #ça copie l'image dans une variable img2
    largeur, longueur = image.width, image.height
    #ça définit la variable largeur à la largeur de l'image et la variable longueur à la longueur de l'image
    for i in range (16):
    #ça répète ce qu'il y a dans la boucle 16 fois
        mosaique+=[img2.crop(((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))]
        #ça divise l'image en plusieurs morceaux et on met tous les morceaux 
    shuffle(mosaique)
    #ça mélange tous les morceaux de l'image de façon aléatoire
    for i in range(16):
    #ça répète ce qu'il y a dans la boucle 16 fois
        image.paste(mosaique[i],((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))
        #ça modifie l'image avec les bouts d'image qui ont été mélangés et les colle dans dans l'image
    image.show()
    #ça montre l'image modifiée

def noir_et_blanc(image,seuil):
    """noir_et_blanc
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    None.
"""
    image_nb=image.copy()
    #ça copie l'image dans une variable image_nb
    for x in range (image_nb.width):
    #ça regarde la largeur de l'image
        for y in range(image_nb.height):
        #ça regarde la longueur de l'image
            rouge=image_nb.getpixel((x,y))[0]
            #ça prend la valeur de la couleur rouge de chaque pixel et la met dans la variable rouge
            bleu=image_nb.getpixel((x,y))[1] 
            #ça prend la valeur de la couleur bleue de chaque pixel et la met dans la variable bleu
            vert=image_nb.getpixel((x,y))[2] 
            #ça prend la valeur de la couleur verte de chaque pixel et la met dans la variable vert
            moyenne=(rouge+bleu+vert)//3
            #ça fait la moyenne de toutes les couleurs de chaque pixel
            if moyenne > seuil:
            #si la moyenne de toutes les couleurs de chaque pixel est supérieure au seuil rentré au début
                image_nb.putpixel((x,y),(255,255,255))
                #ça remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du blanc
            else:
            #sinon si la moyenne de toutes les couleurs de chaque pixel est inférieure au seuil rentré au début
                image_nb.putpixel((x,y),(0,0,0))
                #ça remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du noir
    image_nb.show()
    #ça montre l'image modifiée


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
