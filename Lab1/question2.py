from tkinter import *
from tkinter.ttk import * 

content = """I'm baby thundercats pickled la croix freegan, nostrud in vice 
occaecat minim. Bespoke kitsch vexillologist consequat portland, 
mlkshk distillery disrupt nisi excepteur. Cupidatat tofu polaroid dreamcatcher 
trust fund art party pork belly af knausgaard hell of viral hammock. Readymade 
iPhone shoreditch leggings ad. Deserunt quis distillery before they sold out, 
artisan humblebrag meh waistcoat DIY sed. Lomo typewriter plaid man bun, banjo 
godard freegan air plant. Cred ea velit, sunt single-origin coffee bushwick et. 
Jianbing ea austin 8-bit gluten-free selfies kombucha wayfarers street art 
humblebrag four loko eiusmod. Vape crucifix iceland meggings non hot chicken 
ennui mumblecore labore et. Four dollar toast flexitarian vexillologist, 
affogato street art air plant id culpa. VHS roof party magna excepteur 
gluten-free in. Chia banjo pop-up ut veniam dolor unicorn helvetica gochujang 
small batch bespoke aliquip. Shaman occaecat franzen four loko, fugiat edison 
bulb la croix mollit next level cold-pressed. Four dollar toast ex venmo 
williamsburg celiac XOXO live-edge plaid YOLO fingerstache pop-up deep v. 
Sriracha biodiesel umami fixie lyft readymade venmo truffaut subway tile pug 
tumblr gochujang activated charcoal pop-up. Taxidermy deep v pork belly franzen 
mustache dolore humblebrag cliche velit selfies. Non church-key venmo elit 
unicorn tacos duis ex four dollar toast flannel try-hard microdosing. 
Exercitation qui chartreuse biodiesel ramps."""

window = Tk()
text_window = Text(window, width=24, height=10, wrap = NONE)
text_window.insert(END, content)

v_scrollbar = Scrollbar(window, orient=VERTICAL)
v_scrollbar.pack(side = RIGHT, fill = Y)
v_scrollbar.config(command = text_window.yview)

h_scrollbar = Scrollbar(window, orient=HORIZONTAL)
h_scrollbar.pack(side = BOTTOM, fill = X)
h_scrollbar.config(command = text_window.xview)


text_window.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
text_window.pack()

window.mainloop()