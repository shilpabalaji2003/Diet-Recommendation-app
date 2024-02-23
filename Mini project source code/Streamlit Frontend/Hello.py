import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

background_image = 'Streamlit Frontend\pages\Private vs_ Company-Backed Caregivers - Cahoon Care Associates.jpeg'

# Write custom CSS to set the background image
custom_css = f"""
    <style>
        body {{
            background-image: url('{background_image}');
            background-size: cover;
        }}
    </style>
"""

# Inject the custom CSS into your Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

st.write("# Welcome to Diet Recommendation System! 👋")

st.sidebar.success("Select a recommendation option")

st.markdown("As we gracefully age, our bodies change, and so do our nutritional needs. But that doesn't mean saying goodbye to flavor or fun! Welcome to the diet recommendation website and join us on a plate-by-plate exploration of nutrition, where health meets taste, and every bite empowers you to savor the best years yet!")