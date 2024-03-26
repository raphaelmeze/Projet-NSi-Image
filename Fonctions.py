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
