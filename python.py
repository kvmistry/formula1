import streamlit as st
import webbrowser
from PIL import Image

st.set_page_config(page_title='Data Analytics Project', page_icon='favicon.png', layout="centered", initial_sidebar_state="auto")


st.markdown(
'''
<font color='Red' size='25'><b>Welcome to Data Analytics Project!!</b></font>
'''
,unsafe_allow_html=True)
st.markdown(
'''
<font color='Red' size='5'>Group 1 : Too Fast Too Furious</font>
'''
,unsafe_allow_html=True)

st.markdown('Dataset : '
'''
<a href="https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020">Formula 1 (F1)</a>''',
unsafe_allow_html=True,

)


st.markdown('Group members:'
'''
 - Chandni S. Patel
 - Forum Mathuria
 - Jatin Mahale
 - Joy Mehta
 - Kashyap Mistry
'''
)

st.markdown(
'''
<style>
body {
  background-image: url('https://media.speedcafe.com/wp-content/uploads/2017/06/Renault-F1.jpgsssss');
}
</style>
'''
, unsafe_allow_html=True)

K_Q1 = 'Q) Who has the highest number of fastest lap times across every circuit?'
C_Q1 = 'Q) Which driver has won maximum races?'
C_Q2 = 'Q) Do fast pit stops contribute to winning a race?'
JO_Q1 = 'Q) Which is the most successful constructor?'
JA_Q1 = 'Q) How have lap time and pit stops change over the years? '
F_Q1 = 'Q) What are the maximum number of wins by a single driver during each F1 season?'
F_Q2 = 'Q) Determine Top 10 Driver - Constructor Pair'
F_Q3 = 'Q) Which country hosted most races?'

option = st.selectbox('Select one question', ['...', K_Q1, C_Q1, C_Q2, JO_Q1, JA_Q1, F_Q1, F_Q2, F_Q3])


K_NB = 'K_NB.html'
C_NB = 'C_NB.html'
JO_NB = 'JO_NB.html'
JA_NB = 'JA_NB.html'
F_NB_1 = 'F_NB_1.html'   
F_NB_2 = 'F_NB_2.html'
F_NB_3 = 'F_NB_3.html'

#Kashyap
if option == K_Q1:
    st.markdown(K_Q1)
    K_Q1_IMG = Image.open('K_Q1_IMG.png')
    st.image(K_Q1_IMG, width=500)
    st.subheader('Insights!')
    st.markdown('We can observe that Lewis Hamilton has the highest number of fastest lap times over all the circuits followed by Sebastian Vettel and Max Verstappen.')
    if st.button('View Notebook'):
        webbrowser.open_new_tab(K_NB)
    
#Chandni
if option == C_Q1:
    st.markdown(C_Q1)
    C_Q1_IMG = Image.open('C_Q1_IMG.png')
    st.image(C_Q1_IMG, width=700)
    st.subheader('Insights!')
    st.markdown('From the piechart, we can conclude that Lewis Hamilton has won the maximum numbers of races with 103 wins followed by Prost and Schumacher')
    if st.button('View Notebook'):
        webbrowser.open_new_tab(C_NB)
    
    
if option == C_Q2:
    st.markdown(C_Q2)
    C_Q2_IMG = Image.open('C_Q2_IMG.png')
    st.image(C_Q2_IMG, width=700)
    st.subheader('Insights!')
    st.markdown('What is pit stop and why it is imp? They replace tires, refuel, repair damaged wings or make other modifications to the car to change the down-force and improve performance. In order to do this analysis, I have choosen random races to find out whether pitstops affects in winning a race. From raceId 841 on ‘Position 1’  has taken 2 pit stops for (1st  at 21.6 and 2nd at 24.03 )  total = 45.9 less than a minute and ‘Position 7’  has taken 3 pit stops for (1st  at 23.8 and 2nd at 24.09 and 3rd at 24.5 ) total = 72.39 which is 1min 12sec. In both the position 1 and 7 has difference of 43sec. From ’raceId 1086’ on ‘Position 1’  has taken 2 pit stops for (1st  at 21.2 and 2nd at 21.3 )  total = 42.5 and ‘Position 7’  has taken 2 pit stops for (1st  at 21.8 and 2nd at 23.5 ) total = 45.3. In both the position 1 and 7 has difference of 4sec. Both of them have taken 2 pit stops. From both the graph we conclude that Yes, fast pitstops do contribute in wining the race. ')


    if st.button('View Notebook'):
        webbrowser.open_new_tab(C_NB)

#Joy
if option == JO_Q1:
    st.markdown(JO_Q1)
    JO_Q1_IMG = Image.open('JO_Q1_IMG.png')
    st.image(JO_Q1_IMG, width=700)
    st.subheader('Insights!')
    st.markdown('This bar chart represents the relationship between the constructor I.d and the points each constructor contributes, and the leading constructor is Ferrari with 86138 points. So, Ferrari is the best constructor.')
    if st.button('View Notebook'):
        webbrowser.open_new_tab(JO_NB)

#Jatin
if option == JA_Q1:
    st.markdown(JA_Q1)
    st.text('Lap time')
    JA_Q1_IMG = Image.open('JA_Q1_IMG.png')
    st.image(JA_Q1_IMG, width=700)
    st.subheader('Insights!')
    st.markdown('The below double line graph depicts the total miliseconds taken by each lap as an avaerage in 2 categories. The categories are 1950-2009 and 2011-2019. the lap times in 2011-2019 are more compared to the 1950-2009 lap times. The maximum lap times was in the 25 lap time. The year 1950-2009 has a constant lap duration across all the laps. The lap time across all the years decreases as the lap count increases.')
    
    st.markdown('Pit stop time')
    JA_Q2_IMG = Image.open('JA_Q2_IMG.png')
    st.image(JA_Q2_IMG, caption = 'data', width=700)
    st.subheader('Insights!')
    st.markdown('The below line graph tells the total number of milliseconds taken in a lap for pit stops.The pitstop time increases and decreases, but the increase is double after every downfall.')
    if st.button('View Notebook'):
        webbrowser.open_new_tab(JA_NB)
    
#Forum
if option == F_Q1:
    st.markdown(F_Q1)
    F_Q1_IMG = Image.open('F_Q1_IMG.png')
    st.image(F_Q1_IMG, caption = 'data', width=1000)
    st.subheader('Insights!')
    st.markdown('There doesn’t seem to be a significant pattern for the races won by a single driver across seasons however the numbers have been on the lower side from 2005 to 2012 (exception for 2011) as compared to the other years from which we can say that there was tough competition between the drivers specifically during these years.')
    if st.button('View Notebook'):
            webbrowser.open_new_tab(F_NB_1)
            
if option == F_Q2:
    st.markdown(F_Q2)
    F_Q2_IMG = Image.open('F_Q2_IMG.png')
    st.image(F_Q2_IMG, caption = 'data', width=1000)
    st.subheader('Insights!')
    st.markdown('Lewis Hamilton has been on top of the charts along with Mercedes in terms of the total number of points followed by Max Verstappen from Red bull when looking at a constructor-driver combo. However, Sebastian Vettel takes over Verstappen when considering the total driver points (irrespective of the constructor they were with)')
    if st.button('View Notebook'):
            webbrowser.open_new_tab(F_NB_2)

if option == F_Q3:
    st.markdown(F_Q3)
    F_Q3_IMG = Image.open('F_Q3_IMG.png')
    st.image(F_Q3_IMG, caption = 'data', width=1000)
    st.subheader('Insights!')
    st.markdown('Italy has been the top country to host the Formula 1 races across the world, followed by Germany, UK and USA')
    if st.button('View Notebook'):
            webbrowser.open_new_tab(F_NB_3)     

            
if option == '...':
    st.markdown('Please select a question for insights!')