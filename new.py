from PIL import Image
from random import shuffle


def menu():
    """menu
    Cete fonction permet de faciliter à l'utilsateur l'exécution des fonctions
    en affichant un menu

    Returns
    -------
    None.

    """
    #on affiche un message de bienvenue
    print ("Bienvenue dans le menu du traitement d'images.")
    #on demande à l'utilisateur de choisir une image
    img=input("Quelle image voulez-vous modifiez ? L'image ")
    #on affecte l'image choisie par l'utilisateur à une variable
    image=Image.open(img)
    #on affiche le menu
    print ("Veuillez entrer un chiffre" "\n"
            "1.noir_et_blanc" "\n"
           "2.contours" "\n" "3.premier_plan" "\n"
           "4.mosaique" "\n"
           "5.négatif" "\n"
           "6.Quitter")
    #on affecte la reponse de l'utilisateur à une variable
    reponse_utilisateur=input()
    #on effectue la fonction tant que la reponse de lu'tilisateur est différente de 6
    while reponse_utilisateur!="6":
        #on effectue la fonction si l'utilisateur repond 1
        if reponse_utilisateur=="1":
            #on affecte la reponse de l'utilisateur à une variable seuil
            seuil=int(input("Choisissez un seuil : "))
            #on affecte l'image à une nouvelle variable
            image_noir_et_blanc=noir_et_blanc(image, seuil)
            #on affiche l'image
            image_noir_et_blanc.show()
            #on affiche le menu
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            #on affecte la reponse de l'utilisateur à une variable
            reponse_utilisateur=input()
        #on effectue la fonction si l'utilisateur repond 2
        if reponse_utilisateur=="2":
            #on affecte la reponse de l'utilisateur à une variable seuil
            seuil=int(input("Choisissez un seuil : "))
            #on affecte l'image à une nouvelle variable
            image_contours=contours(image,seuil)
            #on affiche l'image
            image_contours.show()
            #on affiche le menu
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            #on affecte la reponse de l'utilisateur à une variable
            reponse_utilisateur=input()
        #on effectue la fonction si l'utilisateur repond 3
        if reponse_utilisateur=="3":
            #on affecte l'image à une nouvelle variable
            image_premier_plan=premier_plan (image)
            #on affiche l'image
            image_premier_plan.show()
            #on affiche le menu
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            #on affecte la reponse de l'utilisateur à une variable
            reponse_utilisateur=input()
        #on effectue la fonction si l'utilisateur repond 4
        if reponse_utilisateur=="4":
            #on affecte l'image à une nouvelle variable
            image_mosaique=mosaique(image)
            #on affiche l'image
            image_mosaique.show()
            #on affiche le menu
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            #on affecte la reponse de l'utilisateur à une variable
            reponse_utilisateur=input()
         #on effectue la fonction si l'utilisateur repond 5
        if reponse_utilisateur=="5":
            #on affecte l'image à une nouvelle variable
            image_negatif=negatif(image)
            #on affiche l'image
            image_negatif.show()
            #on affiche le menu
            print ("Veuillez entrer un chiffre" "\n"
                    "1.noir_et_blanc" "\n"
                   "2.contours" "\n" "3.premier_plan" "\n"
                   "4.mosaique" "\n"
                   "5.négatif" "\n"
                   "6.Quitter")
            #on affecte la reponse de l'utilisateur à une variable
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
    #on définit la variable mosaique à un tableau vide
    mosaique=[]
    #on copie l'image dans une variable img2
    img3=image.copy()
    #on définit la variable largeur à la largeur de l'image et la variable longueur à la longueur de l'image
    largeur, longueur = image.width, image.height
    #on répète ce qu'il y a dans la boucle 16 fois
    for i in range (16):
        #on divise l'image en plusieurs morceaux
        mosaique+=[img3.crop(((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))]
    #on mélange tous les morceaux de l'image de façon aléatoire    
    shuffle(mosaique)
   #on répète ce qu'il y a dans la boucle 16 fois
    for i in range(16):
         #on modifie l'image avec les bouts d'image qui ont été mélangés et les colle dans dans l'image
        img3.paste(mosaique[i],((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))
    #on montre l'image modifiée  
    return img3


def premier_plan (image):
"""premier_plan
    

    Parameters
    ----------
    image : list
        image

    Returns
    -------
    img2 : list
        image modifiée

"""
    #on copie l'image dans une variable img2
    img2=image.copy()
    #on affecte la réponse de l'utilisateur à la variable r
    r=int(input("Quelle valeur de rouge voulez-vous gardez ?"))
    #on affecte la réponse de l'utilisateur à la variable b
    b=int(input("Quelle valeur de bleu voulez-vous gardez ?"))
    #on affecte la réponse de l'utilisateur à la variable v
    v=int(input("Quelle valeur de vert voulez-vous gardez ?"))
    #on affecte la réponse de l'utilisateur à la variable tolerance
    tolerance=int(input("Quelle tolérance acceptez-vous autour de cette couleur ?"))
    #on parcourt la largeur de l'image
    for x in range (img2.width): 
        #on parcourt la longueur de l'image
        for y in range (img2.height): 
            #on prend la valeur des couleurs de chaque pixel et la met dans la variable rouge
            rouge=img2.getpixel((x,y))[0] 
            #on prend la valeur des couleurs de chaque pixel et la met dans la variable vert
            vert=img2.getpixel((x,y))[1]
            #on prend la valeur des couleurs de chaque pixel et la met dans la variable bleu
            bleu=img2.getpixel((x,y))[2]
            #on effectue la boucle si les couleurs de l'image ne sont pas inférieures à la somme des valeurs des couleurs indiquées par l'utilisateur et la tolérance
            #on effectue la boucle si les couleurs de l'image ne sont pas supérieure à la différence des valeurs des couleurs indiquées par l'utilisateur et la tolérance
            if not((rouge>r-tolerance and rouge<r+tolerance)and(bleu>b-tolerance and bleu<b+tolerance)and(vert>v-tolerance and vert<v+tolerance)):
                #on fait la moyenne des trois variables
                m=(rouge+bleu+vert)//3
                #on remplace les valeurs des couleurs des pixels par les valeurs des couleurs de la moyenne des pixels
                img2.putpixel((x,y),(m,m,m))
    #on retourne l'image modifiée
    return img2
