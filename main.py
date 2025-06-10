import streamlit as st
from streamlit_option_menu import option_menu
st.header("🤖AIML Engineer")
st.subheader("CS graduate")

st.progress(0.5)
st.progress(0.5,text="50%")
st.progress(0.5,text="50%")
st.title("👰🏼‍♂️I am Vaishnavi")
st.text_input("Enter Your name")
st.number_input("Enter Your age")
st.date_input("Enter DOB")
st.checkbox("I agree")
st.radio("Select your gender",["Male","Female"])
st.selectbox("Select your country ",["Male","Female"])
st.multiselect("Select your country ",["Male","Female"])
st.slider(label="Saturation",min_value=0,max_value=100,value=10)


st.write("## This is a text ")
st.write("- This is a text ")
st.code("""
#include <stdio.h>

int main() {
  printf("Hello World!");
  return 0;
}

""",language="c")
st.latex(r"y=mx+c")

st.metric(label="temparature",value="70F",delta="-1.2F")
st.code("""
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
""",language="html")

with st.sidebar :
  select = option_menu(
    menu_title="vinup",
    options=["Home","About","Service"],
    icons=['house','file-person','gear']

  )
if select == "Home":
  st.title("Welcome to Home")
  col1,col2 =st.columns(2)
  with col1:
    st.divider()
    a =st.text_input("Name")
    if st.button("Click"):
      if a == "":
         st.error("Please Enter the name")
      else:
       st.toast("you are verified")
       st.balloons()
  with col2:
     st.divider()
     st.text_input("Email")
     st.image("https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?cs=srgb&dl=pexels-souvenirpixels-414612.jpg&fm=jpg")
elif select == "About":
   st.title("Welcome to About")
elif select == "Service":
   st.title("Welcome to Service")