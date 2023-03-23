import streamlit as st


st.markdown(
        """<style>
        .css-9s5bis.edgvbvh3
        {
                visibility: hidden;
        }
        
        .css-1vbd788.egzxvld2
        {
                visibility: hidden;
        }
        
        </style>""",unsafe_allow_html=True
)
st.markdown("<h1 style ='text-align: center;' >PHYSIPEDIA</h1>", unsafe_allow_html=True)
st.header('Welcome to Physipedia!!')
col1,col2 = st.columns(2)
signin_txt=col1.text('If you already have account please SignIn')
signin= col1.button('SignIn')
signup_txt=col2.text('If you don\'t have an account please signup')
signup= col2.button('SignUp')
if(signin):
        with st.form('login'):
                col3,col4 =st.columns(2)
                login=col3.text_input("Enter Your Username")
                passw= col4.text_input('Enter Your Password')
                btn1=st.form_submit_button('Submit')
                if login == "" and passw == "":
                        st.warning("please fill above fields")
                else:
                        st.warning("Submit Successfully")
                        st.warning('Your Account has been created')
                        
elif(signup):
        with st.form("sign"):
                col5,col6 = st.columns(2)
                f_name=col5.text_input("First name")
                l_name=col6.text_input("Last name")
                passw1= col5.text_input("Enter a password")
                passw2= col6.text_input("Confirm Password")
                btn2=st.form_submit_button('Submit')
a =st.text_input('search your topic hear')
b= st.button('search')


tab1, tab2, tab3 ,tab4 = st.tabs(["Wikipedia", "Britaniaca", "Citiizendium", "Conservapedia"])
with tab1:
        st.subheader('Wikipedia')
        st.write(f'<iframe src="https://en.wikipedia.org/wiki/{a}" style = "width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab2:
        st.subheader('Encyclopedia of Britanica')
        st.write(f'<iframe src="https://www.britannica.com/search?query={a}" style = "width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab3:
        st.subheader('Citizendium')
        st.write(f'<iframe src="https://citizendium.org/wiki/{a}" style="width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab4:
        st.subheader('Conservapedia')
        st.write(f'<iframe src="https://www.conservapedia.com/{a}" style="width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)

"""st.write(
        f'<iframe src="https://en.wikipedia.org/wiki/{a}" style="width:px;height:500px"></iframe>',
        unsafe_allow_html=True)

tab2.subheader("A tab with the data")"""
# a =st.text_input('search your topic hear')
# b= st.button('search')
# st.write(
#         f'<iframe src="https://www.britannica.com/science/{a}" style="width:750px;height:500px"></iframe>',
#         unsafe_allow_html=True)
# if(b):
#     if(a=='electron'):
#         a1 = st.selectbox("related to search result",('Electron (wiki)', 'Electron (Encyclopedia of Britancica)'))
#         if(a1 == 'Electron (wiki)'):
#             st.markdown('[Electron (wiki)](%s)' % electron.electron1)
#         elif(a1 == 'Electron (Encyclopedia of Britancica)'):
#             st.markdown('[Electron (Encyclopedia of britanica)](%s)' % electron.electron2)
    
#     else:
#         st.write('topic is not found')
        
