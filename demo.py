import streamlit as st
from .main import generate

def plot_generation () :
    response = generate(
        query=st.session_state.query,
        max_items=st.session_state.max_items
    )
    
    st.write(response)

st.title("Outfit Creator")
text_input = st.text_input("Enter your prompt", key="query")
if st.checkbox("All options") :
    st.slider("Max Number of items", min_value=2, max_value=6, value=4, key="max_items")
else :
    st.session_state.max_items = 4
    
st.button("Generate", on_click=plot_generation)
def plot_generation () :
    response = generate(
        query=st.session_state.query,
        max_items=st.session_state.max_items
    )
    
    st.session_state.images = [ i.des_filename for i in response ]
    

st.title("Outfit Creator")
text_input = st.text_input("Enter your prompt", key="query")
if st.checkbox("All options") :
    st.slider("Max Number of items", min_value=2, max_value=6, value=4, key="max_items")
else :
    st.session_state.max_items = 4
    
st.button("Generate", on_click=plot_generation)

if st.session_state.images is not None :
    for img_name in st.session_state.images :
        st.image("datathon/images/" + img_name)