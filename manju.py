import streamlit as st
st.title("electricity bill calculator")
first_line=st.number_input("enter no.of units:")
second_line=st.selectbox("enter connection_type(domestic/commercial):")
bill=0
if first_line<=100:
  bill=(first_line*5)
elif first_line<=200:
  bill=(100*5)+(first_line-100)*7
else:
  bill=(100*5)+(100*7)+(first_line-200)*10
if second_line=="commercial":
  bill+=200
  if first_line>300:
    bill+=100
  elif second_line=="domestic":
    if first_line>200:
      bill=first_line-(0.05*bill)
    if st.button("calculate bill"):
        st.success("total bill is",bill)