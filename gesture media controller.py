#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##improve this by using left and right hand detection which will help classify if the thumb is open or not 
##if left hand the run this block of code:
  ##      if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > threshold:
    #    cnt += 1
    #if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > threshold:
     #   cnt += 1
    #if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > threshold:
      #  cnt += 1   
    #if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > threshold:
     #   cnt += 1
    #if (lst.landmark[4].x*100 - lst.landmark[5].x*100) > 5: 
     #   cnt += 1

    #elif i.e if right hand run this block of code:
            #if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > threshold:
        #cnt += 1
    #if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > threshold:
     #   cnt += 1
    #if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > threshold:
     #   cnt += 1   
    #if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > threshold:
      #  cnt += 1
    #if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 5: 
     #   cnt += 1
##also just dont do it for left and right do it for left back,left front, right back and right front
##side note le ft back = right front and right back = left front


# In[138]:


import cv2
import mediapipe as mp
import pyautogui as pag
import time


# In[139]:


def count_fingers(lst):
    cnt = 0
    
    
    threshold = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2
    
    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > threshold:
        cnt += 1
    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > threshold:
        cnt += 1
    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > threshold:
        cnt += 1   
    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > threshold:
        cnt += 1
    if (lst.landmark[4].x*100 - lst.landmark[5].x*100) > 5: 
        cnt += 1
    return cnt


# In[140]:


cap = cv2.VideoCapture(1) ##definig variable to store the camera


# In[141]:


drawing  = mp.solutions.drawing_utils #define drawing variable 
hands = mp.solutions.hands #define hands variable to store the hands from mediapipe
hand_obj = hands.Hands(max_num_hands=1)#creating object hand and defineing the number of hands we want mediapipe to detect in one frame as 1 
start_init = False
prev = -1


# In[142]:


while True:
    end_time = time.time()
    _, frm = cap.read() ##define the camera window frame
    frm = cv2.flip(frm, 1) ##flips the frame so it does not appear mirror like 
    
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
    
    if res.multi_hand_landmarks:
        
        hand_keyPoints = res.multi_hand_landmarks[0] 
        
        cnt = count_fingers(hand_keyPoints)
        if not(prev==cnt):
            if not (start_init):
                start_time = time.time()
                start_init = True
            elif(end_time-start_time) > 1:
                if (cnt == 1):
                    pag.press("right")
                elif (cnt == 2):
                    pag.press("left")
                elif (cnt == 3):
                    pag.press("up")
                elif (cnt == 4):
                    pag.press("down")
                elif (cnt == 5):
                    pag.press("space")
                    
                prev = cnt
                start_init = False
        
        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)
    
    
    
    cv2.imshow("window", frm)##shows the camera window to the user
   
    if cv2.waitKey(1) == 27: ##if user presses esc key the camera window frame closes
        cv2.destroyAllWindows()
        cap.release() ##release the camera window frame to other applications so those applications can use it
        break 
      


# In[ ]:




