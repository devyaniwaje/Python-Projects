#!/usr/bin/env python
# coding: utf-8

# In[1]:


import moviepy.editor


# In[2]:


from  tkinter.filedialog import *
vid=askopenfilename()
video=moviepy.editor.VideoFileClip(vid)
aud=video.audio
aud.write_audiofile("demo.mp3")
print("---End---")


# In[ ]:




