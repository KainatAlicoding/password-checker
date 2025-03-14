import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    
    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Upper and lower case check
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    
    # Number check
    if re.search("\d", password):
        strength += 1
    
    # Special character check
    if re.search("[@$!%*?&]", password):
        strength += 1
    
    # Determine strength level
    if strength == 1:
        remarks = "Very Weak"
    elif strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 4:
        remarks = "Strong"
    
    return strength, remarks

def main():
    st.title("🔒 Password Strength Checker")
    st.write("Enter a password to check its strength.")
    
    password = st.text_input("Enter Password", type="password")
    
    if password:
        strength, remarks = check_password_strength(password)
        
        st.write(f"**Strength Level:** {strength}/4")
        st.write(f"**Remarks:** {remarks}")
        
        # Progress bar
        st.progress(strength / 4)

if __name__ == "__main__":
    main()
