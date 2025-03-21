import streamlit as st
import re # Python ka built-in module hai jo regex (Regular Expressions) se related functions provide karta hai.

st.set_page_config(page_title='Password Strength Checker', page_icon='🔒')
st.title('Password Strength Checker')


st.markdown("""
## 🔐 Welcome to the Password Strength Checker!
Type your password in the box below, then click the button to see how secure it is.
Let’s build a strong password and boost your online safety! 💪
""")

# user say input leinge. password type password isliye humein eye symbol dikhay ga proper password view.
password = st.text_input('Enter your password here', type='password') 

# empty list or variable banaya.
feedback = []
score = 0

# agar password hai tw.
if password:

    if len(password) >= 8:
        score += 1
    else:
        feedback.append('❌ Password must be at least 8 characters long.')
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score +=1
    else:
        feedback.append('❌ Password should contain both uppercase and lowercase characters.')
    
    if re.search(r'[\d]', password):
        score += 1
    else:
        feedback.append('❌ Password should contain atleast one digit.')
    
    if re.search(r'[!@#$-*]', password):
        score += 1
    else: 
        feedback.append('❌ Password should contain atleast one special character (!@#$-*)')

    if score == 4 :
        feedback.append('✅ Your password is strong 🎉')
    elif score == 3 :
        feedback.append('🟡 Your password is medium strength. it could be stronger.')
    else:
        feedback.append('🔴 Your password is very weak. Please make it stronger.')
    
    #loop agar feedback main kuch hai tw woo print
    if feedback:
        st.markdown('### Improvement Suggestions')
        for feed in feedback:
            st.write(feed)
    
else:
    st.info('Please enter your password to get started.')

   