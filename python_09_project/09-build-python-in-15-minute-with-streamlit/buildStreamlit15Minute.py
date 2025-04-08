import streamlit as st

st.title("Simple Calculator")
st.write("This is a simple calculator that can perform addition, subtraction, multiplication, and division.")

def Calculator(num1:int,num2:int,operation:str)->int:
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Operation '{operation}' not recognized.")

num1 = st.number_input("Enter first number:", value=0)
num2 = st.number_input("Enter second number:", value=0)
operation = st.radio("Select operation:", ('add', 'subtract', 'multiply', 'divide'))

if st.button("Calculate"):
    try:
        result = Calculator(num1, num2, operation)
        st.write(f"The result of {num1} {operation} {num2} is: {result}")
    except ZeroDivisionError as e:
        st.error(e)
    except ValueError as e:
        st.error(e)
    except Exception as e:
        st.error(f"An error occurred: {e}")