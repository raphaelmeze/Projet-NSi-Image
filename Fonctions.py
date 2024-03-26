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
