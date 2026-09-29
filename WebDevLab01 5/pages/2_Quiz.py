import time
import streamlit as st

st.title("🧙✨The Sorting Hat✨🔮🪄") 
scores = {"Gryffindor" : 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin":0 }

#Question 1
traits = st.multiselect("Pick up to two traits:", ["Brave", "Loyal", "Clever", "Ambitious"], max_selections = 2)

if "Brave" in traits:
    scores["Gryffindor"] += 1
if "Loyal" in traits:
    scores["Hufflepuff"] += 1
if "Clever" in traits:
    scores["Ravenclaw"] += 1
if "Ambitious" in traits:
    scores["Slytherin"] += 1
          

#Question 2

          
midnight = st.radio("It's midnight, What are you up to?:", ["1", "📚 2", "3", "💛 4"])#NEW

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("Images/sneakingout.jpg", width = 200)
    st.caption("1: Sneaking out")
with col2:
    st.image("Images/library.jpg", width = 200)
    st.caption("2: Studying in the library")
with col3:
    st.image("Images/spells.png", width = 200)
    st.caption("3: Practicing advanced spells")
with col4:
    st.image("Images/friend.jpeg", width = 200)
    st.caption("4: Chatting with a friend")
    
if midnight == "1":
    scores["Gryffindor"] += 1
if midnight == "2":
    scores["Ravenclaw"] += 1
if midnight == "3":
    scores["Slytherin"] += 1
if midnight == "4":
    scores["Hufflepuff"] += 1
    
#Question 3

competitiveness = st.slider("How much do you care about winning?", 1, 10)#NEW

if competitiveness >= 8:
    scores["Slytherin"] += 1
if 5 <= competitiveness <= 7:
    scores["Gryffindor"] += 1
if competitiveness <= 3:
    scores["Hufflepuff"] += 1

#Question 4
    
risk = st.number_input("On a scale from 1 - 10, How likely are you to take risks for a friend? (type value) ", min_value = 1, max_value = 2, step = 1)

if risk >= 8:
    scores["Gryffindor"] += 1
    
elif 5 <= risk <= 7:
    scores["Ravenclaw"] += 1
    
elif risk <= 4:
    pass

#Question 5
wand = st.selectbox("Chose a wand core:", ["Dragon Heartstring", "Phoenix Feather", "Unicorn Hair", "Veela Hair"])#NEW

if wand == "Dragon Heartstring":
    scores["Slytherin"] += 1
    
if wand == "Phoenix Feather":
    scores["Gryffindor"] += 1
    
if wand == "Unicorn Hair":
    scores["Hufflepuff"] += 1
    
if wand == "Veela Hair":
    scores["Ravenclaw"] += 1




#Results

if st.button("Reveal my house!🪄"):

    with st.spinner ("🧙‍♂️*hmmm..difficult. Very difficult. Plenty of courage I see. Not a bad mind either...*"):
        time.sleep(3)
                  
    result = max(scores, key = scores.get)
    st.write(f"🎉 Congrats! you're in **{result}**!")

    if result == "Gryffindor":
        st.info("🦁 You're a bold one! Your courage, nerve, and curiosity set you apart.")

    elif result == "Hufflepuff":
        st.info("🦡You're a loyal soul! A strong work ethic paired with a kind heart is truly a good combo.")

    elif result == "Ravenclaw":
        st.info("🦅You have a sharp mind! You're wisdom and lover for learning will take you far.")
        
    elif result == "Slytherin":
        st.info("🐍You're an ambitious one! Such leadership, wit, and drive will no doubt carve a great future.")  
        
    st.image(f"Images/{result.lower()}.jpg", width = 200)
    st.balloons()

    
    





    

    
    



    
