#!/usr/bin/env python
# coding: utf-8

# In[112]:


import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from PIL import ImageEnhance

st.title("Kubettize App for Pyssla")

st.write("""#### 
A simple web application that allows you to pixelize images in order to make them easily achievable with Pyssla or similar.
Made for my son on October 10, 2020""")

image = Image.open('KUBETTIZE.png')
st.sidebar.image(image, use_column_width=True)

uploaded_file1 = st.sidebar.file_uploader("Carica l'immagine da cubettizare", type=["jpg"])


if uploaded_file1 is not None:
    # Open Paddington
    st.write('''### Immagine originale''')
    img = Image.open(uploaded_file1)
    st.image(img, use_column_width=True)
    # Resize smoothly down to 16x16 pixels

    cube = st.sidebar.slider('definizione', 20,60, 30)
#     cube = int(cube)
    contrast = st.sidebar.slider('Contrasto', 1,10, 10)/10
    colore = st.sidebar.slider('Colore', 1,10, 10)/10
    luminosita = st.sidebar.slider('Luminosità', 1,10, 10)/10
    nitidezza = st.sidebar.slider('Nitidezza', 1,10, 10)/10
    
   

    imgSmall = img.resize((cube,cube),resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size,Image.NEAREST)

    # Save
    enhancer = ImageEnhance.Contrast(result)
    result = enhancer.enhance(contrast)
    
    enhancer2 = ImageEnhance.Color(result)
    result1 = enhancer2.enhance(colore)
    
    enhancer3 = ImageEnhance.Brightness(result1)
    result2 = enhancer3.enhance(luminosita)
    
    enhancer4 = ImageEnhance.Brightness(result2)
    result3 = enhancer3.enhance(luminosita)
    
#     st.write(contrast, colore, luminosita )
    
    
    
#     fig = plt.imshow(result)
    st.write('''### Immagine modificata''')
    st.image(result3, use_column_width=True)

