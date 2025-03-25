import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")

st.title("This is a header")
st.header("This is a subheader")
st.text("This is text")
st.markdown("This is some **markdown**")

# success, info, warning, error and exception

st.success("This is a sucess message")
st.info("This is a info message")
st.warning("This is a warning message")
st.error("This is a error message")
st.exception(ValueError("This is a exception message"))

#exception for division by zero
exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)
st.code("This is code")
st.image("https://cdn.pixabay.com/photo/2018/08/04/11/30/draw-3583548_1280.png")

#checkbox
if st.checkbox("Show Message"):
    st.write("You checked the box! ")

status = st.radio("Select Gender", ("Male","Female"))
if status == "Male":
    st.write("Male")
else:
 st.write("Female")

#selctbox
neta = st.selectbox("Netaharu",["oli","deuba"])
st.write("your neta is ", neta)
#multiselect box
heroes =  st.multiselect("Heroes:",["heroines","ali"])
if heroes:  # If the list is not empty
    st.write("Your hero is:", ", ".join(heroes))
else:
    st.write("No hero selected. Please choose one.")
st.button("Click me ")
if st.button("about"):
    st.text("This is a button.")

name = st.text_input("Enter your name","Type here...")
if st.button("Submit"):
    result = "Hello " + name
    st.success(result)

slider =  st.slider("Select a slider",0,100,50)
st.text("Your level is {slider}")

