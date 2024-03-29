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
            choix=input("Voulez vous affichez la photo ")
            if choix=='oui':
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
            choix=input("Voulez vous affichez la photo ")
            if choix=='oui':
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
            choix=input("Voulez vous affichez la photo ")
            if choix=='oui':
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
            choix=input("Voulez vous affichez la photo ")
            if choix=='oui':
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
            choix=input("Voulez vous affichez la photo ")
            if choix=='oui':
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
    return image_nb
    
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
    mosaique=[]
    img2=image.copy()
    largeur, longueur = image.width, image.height
    for i in range (16):
        mosaique+=[img2.crop(((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))]
    shuffle(mosaique)
    for i in range(16):
        img2.paste(mosaique[i],((i//4)*(largeur//4),(i%4)*(longueur//4),(i//4)*(largeur//4)+(largeur//4),(i%4)*(longueur//4)+(longueur//4)))
    return img2

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
