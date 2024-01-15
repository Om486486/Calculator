import streamlit as st

st.success("# Simple Calculator")

# Define the Operation
operations={
    "+" : lambda x,y:x+y,
    "-" : lambda x,y:x-y,
    "*" : lambda x,y:x*y,
    "/" :lambda x,y:x/y,
}

#Get the user input
num1=st.number_input("Enter the first Number :")
num2=st.number_input("Enter the Second Number :")

# Select the Operation
operation=st.selectbox("Select the Operation: ",list(operations.keys()))

# Calculate the result
result=operations[operation](num1,num2)

# Display the result
st.write("The result is : ",result)