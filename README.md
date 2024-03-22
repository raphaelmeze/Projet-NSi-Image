# Projet-NSi-Image
Ceci est un projet de traitement d'images avec python réalisé en groupe de trois

La première fonction marche, la deuxième à tester j'ai eu un petit problème qui m'empêche de tester.
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
