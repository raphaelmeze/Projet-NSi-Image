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
    #on parcourt la largeur de l'image
    for x in range (image.width): 
        #on parcourt la hauteur de l'image
        for y in range (image.height): 
            #on récupère les valeurs de la couleur rouge pour chaque coordonnés des pixels
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

def noir_et_blanc(image,seuil):
    for x in range (image.width):
        for y in range(image.height):
            rouge=image.getpixel((x,y))[0]
            bleu=image.getpixel((x,y))[1] 
            vert=image.getpixel((x,y))[2] 
            moyenne=(rouge+bleu+vert)//3
            if moyenne > seuil:
                image.putpixel((x,y),(255,255,255))
            else:
                image.putpixel((x,y),(0,0,0))
    image.show()

def negatif(image):
    for x in range (image.width): 
        for y in range (image.height): 
            r, v, b=image.getpixel((x,y))
            image.putpixel((x,y),(255-r,255-v,255-b)) 
    image.show() 
def premier_plan (image,):
    r=int(input("Quelle valeur de rouge voulez-vous gardez ?"))
    b=int(input("Quelle valeur de bleu voulez-vous gardez ?"))
    v=int(input("Quelle valeur de vert voulez-vous gardez ?"))
    tolerance=int(input("Quelle tolérance acceptez-vous autour de cette couleur ?"))
    for x in range (image.width): 
        for y in range (image.height): 
            rouge=image.getpixel((x,y))[0] 
            vert=image.getpixel((x,y))[1]
            bleu=image.getpixel((x,y))[2]
            if not((rouge>r-tolerance and rouge<r+tolerance)and(bleu>b-tolerance and bleu<b+tolerance)and(vert>v-tolerance and vert<v+tolerance)):
                m=(rouge+bleu+vert)//3
                image.putpixel((x,y),(m,m,m))
    image.show()
