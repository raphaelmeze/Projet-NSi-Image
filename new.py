from PIL import Image
from random import shuffle


def menu():
    print ("Bienvenue dans le menu du traitement d'images.")
    img=input("Quelle image voulez-vous modifiez ? L'image ")
    image=Image.open(img)
    print ("Veuillez entrer un chiffre" "\n"
            "1.noir_et_blanc" "\n"
           "2.contours" "\n" "3.premier_plan" "\n"
           "4.mosaique" "\n"
           "5.négatif" "\n"
           "6.Quitter")
    reponse_utilisateur=input()
    while reponse_utilisateur!="6":
        if reponse_utilisateur=="1":
            seuil=int(input("Choisissez un seuil : "))
            image_noir_et_blanc=noir_et_blanc(image, seuil)
            image_noir_et_blanc.show()
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            reponse_utilisateur=input()
        if reponse_utilisateur=="2":
            seuil=int(input("Choisissez un seuil : "))
            image_contours=contours(image,seuil)
            image_contours.show()
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            reponse_utilisateur=input()
        if reponse_utilisateur=="3":
            image_premier_plan=premier_plan (image)
            image_premier_plan.show()
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            reponse_utilisateur=input()
        if reponse_utilisateur=="4":
            image_mosaique=mosaique(image)
            image_mosaique.show()
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            reponse_utilisateur=input()
        if reponse_utilisateur=="5":
            image_negatif=negatif(image)
            image_negatif.show()
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            reponse_utilisateur=input()
    #on affiche au revoir et on sort du programme menu
    print("Au revoir !")
    
def noir_et_blanc(image,seuil):
    """noir_et_blanc
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    image_nb : list
"""
    #on copie l'image dans une variable image_nb
    image_nb=image.copy()
    #on regarde la largeur de l'image
    for x in range (image_nb.width):
        #on regarde la longueur de l'image
        for y in range(image_nb.height):
            #on prend la valeur de la couleur rouge de chaque pixel et la met dans la variable rouge
            rouge=image_nb.getpixel((x,y))[0]
            #on prend la valeur de la couleur bleue de chaque pixel et la met dans la variable bleu
            bleu=image_nb.getpixel((x,y))[1] 
            #on prend la valeur de la couleur verte de chaque pixel et la met dans la variable vert
            vert=image_nb.getpixel((x,y))[2] 
            #on fait la moyenne de toutes les couleurs de chaque pixel
            moyenne=(rouge+bleu+vert)//3 
            #si la moyenne de toutes les couleurs de chaque pixel est supérieure au seuil rentré au début
            if moyenne > seuil:
                #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du blanc
                image_nb.putpixel((x,y),(255,255,255))
            #sinon si la moyenne de toutes les couleurs de chaque pixel est inférieure au seuil rentré au début
            else:
                #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du noir
                image_nb.putpixel((x,y),(0,0,0))
    #on retourne l'image modifiée
    return image_nb
    
def negatif(image):
    """negatif
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    img2 : list
"""
    #on copie l'image dans une variable image_nb
    img2=image.copy()
    #on regarde la largeur de l'image
    for x in range (img2.width): 
        #on regarde la longueur de l'image
        for y in range (img2.height): 
            #on prend toutes les couleurs de tous les pixels de l'image
            r, v, b=img2.getpixel((x,y))
            #on remplace les pixels par leur pixels négatifs en rajoutant 255 à chaque couleur de chaque pixel
            img2.putpixel((x,y),(255-r,255-v,255-b)) 
    #on retourne l'image modifiée 
    return img2
    
def niveaux_de_gris(image): 
    """niveaux_de_gris
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    img2 : list
"""
    #on copie l'image dans une variable img2
    img2=image.copy()
    #on regarde la largeur de l'image
    for x in range (img2.width): 
        #on regarde la longueur de l'image
        for y in range (img2.height): 
            #on prend la valeur de la couleur rouge de chaque pixel et la met dans la variable rouge
            rouge=img2.getpixel((x,y))[0] 
            #on prend la valeur de la couleur bleue de chaque pixel et la met dans la variable bleu
            bleu=img2.getpixel((x,y))[1] 
            #on prend la valeur de la couleur verte de chaque pixel et la met dans la variable vert
            vert=img2.getpixel((x,y))[2] 
            #on fait la moyenne de toutes les couleurs de chaque pixel
            m=(rouge+bleu+vert)//3 
            #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs de la moyenne des pixels
            img2.putpixel((x,y),(m,m,m)) 
    #on montre l'image modifiée
    return img2 
    
def contours(image,seuil):
    """contours
    

    Parameters
    ----------
    image : list
        image
    seuil : int

    Returns
    -------
    img2 : list
"""
    #on copie l'image dans une variable img2
    img2=image.copy()
    #on effectue la fonction niveaux_de_gris
    niveaux_de_gris(img2)
    #on regarde la largeur de l'image en y soustrayant 1
    for x in range (img2.width-1): 
        #on regarde la longueur de l'image en y soustrayant 1
        for y in range (img2.height): 
            #on demande si on est à la bordure gauche de l'image
            if x==0: 
                #on prend la valeur des couleurs de chaque pixel et la met dans la variable couleur1
                couleur1=img2.getpixel((x,y))[0]  
                #on prend la valeur des couleurs de chaque pixel et la met dans la variable couleur2
                couleur2=img2.getpixel((x+1,y))[0]
                #on fait la différence en valeur absolue
                difference=abs(couleur1-couleur2)
                #on regarde si la différence obtenue est supérieur au seuil donné au début
                if difference>seuil: 
                    #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du blanc
                    img2.putpixel((x,y),(255,255,255)) 
                #sinon si le seuil est supérieur à la diférence
                else: 
                    #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du noir
                    img2.putpixel((x,y),(0,0,0))
            #sinon si on n'est pas à la bordure de l'image
            else: 
                #on prend la valeur des couleurs de chaque pixel et la met dans la variable couleur1
                couleur1=image.getpixel((x,y))[0] 
                #on prend la valeur des couleurs de chaque pixel et la met dans la variable couleur2
                couleur2=image.getpixel((x+1,y))[0] 
                #on fait la différence en valeur absolue
                difference=abs(couleur1-couleur2) 
                #on regarde si la différence obtenue est supérieur au seuil donné au début
                if difference>seuil:
                    #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du blanc
                    img2.putpixel((x,y),(255,255,255))  
                #sinon si le seuil est supérieur à la diférence
                else:
                    #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs des pixels du noir
                    img2.putpixel((x,y),(0,0,0)) 
    #on montre l'image modifiée
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

def premier_plan (image):
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
