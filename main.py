import fitz

def overlay_text(input_pdf, output_pdf, text,y, page_num=0):

    doc = fitz.open(input_pdf)
    # font = fitz.Font("CustomFont", fontfile="fonts/GlacialIndifference-Regular.ttf")

    page = doc[page_num]

    text_color = (0, 0, 0)  
    font_size = 57

    page_width = page.rect.width
    text_box = fitz.Rect(0, y-32, page_width, y + font_size + 30)
    
    page.insert_textbox(text_box, text, fontsize=font_size, fontname="CustomFont", color=text_color, align=1,fontfile="fonts/Belleza-Regular.ttf")
    # page.insert_text((x, y), text, fontsize=font_size,fontname="CustomFont", color=text_color,fontfile="fonts/GlacialIndifference-Regular.ttf")


    doc.save(output_pdf)
    doc.close()
    print(f"Overlay added. Saved as {output_pdf}")


import csv

data_file = "participants.csv"

# for testing, uncomment below line
# data_file = "test_data.csv" 

import os
if not os.path.exists("output"):
    os.makedirs("output")
    print("created output folder as it does not exist.")

with open(data_file,'r',newline='',encoding='utf-8') as f:
    r = list(csv.reader(f))
    names = []
    for i in r:
        names.append(i[0])

    template = "template/template.pdf"
    for name in names:
        overlay_text(template,f"output/{name.strip()}.pdf",name.strip().upper(),304)

    

# overlay_text("template.pdf", "output.pdf", "Overlay Text", 100, 100)
