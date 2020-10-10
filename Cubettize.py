#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.title("Kubettize App for Pyssla")

image = Image.open('KUBETTIZE.png')
st.sidebar.image(image, use_column_width=True)

uploaded_file1 = st.sidebar.file_uploader("Carica l'immagine da cubettizare", type=["jpg"])


if uploaded_file1 is not None:
    # Open Paddington
    st.write('''### Immagine originale''')
    img = Image.open(uploaded_file1)
    st.image(img, use_column_width=True)
    # Resize smoothly down to 16x16 pixels

    cube = st.sidebar.slider('definizione', 20,60)

    imgSmall = img.resize((cube,cube),resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size,Image.NEAREST)

    # Save
    
#     fig = plt.imshow(result)
    st.write('''### Immagine modificata''')
    st.image(result, use_column_width=True)


# In[3]:





# In[ ]:




