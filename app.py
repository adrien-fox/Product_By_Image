import streamlit as st
import requests
from bs4 import BeautifulSoup
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "Business Rule ToolBox",
                   page_icon = ":fox:",
                   layout = 'wide')

with st.sidebar:

    navigation = option_menu("Navigation", ["Google Images","Regex"],
                            icons=['arrow-left-right', 'bookmark-check',],
                            menu_icon="app-indicator", default_index=0,
                            styles={
        "container": {"padding": "5!important", "background-color": "#00000"},
        "icon": {"color": "#774ee0", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#900000"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if navigation == "Google Images" : 

    col1, col2  = st.columns(2)

    with col1:
        st.header("Enter your list of Product Name")
        product_name = st.text_area("Enter product list","Iphone\nPomme\nPringles")

    with col2:
        st.header("Enter your list of Breadcrumbs")
        breadcrumb_list = st.text_area("Enter beadcrumb list","High Tech\nFruits & Vegetables\nSalty groceries")

    product_list = ','.join(product_name.splitlines())
    product_list = list(product_list.split(","))
    breadcrumb_list = ','.join(breadcrumb_list.splitlines())
    breadcrumb_list = list(breadcrumb_list.split(","))



    def get_image_url(product_name):
        query = product_name
        url = f"https://www.google.com/search?q={query}&tbm=isch"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        img_tag = soup.find("img", {"class": "yWs4tf"})

        if img_tag is not None:
            img_link = img_tag.get("src")
            return st.image(img_link)
        else:
            return None

        
    if st.button("Click to look for Google Images") :

        st.markdown("---")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(product_list[0])
            get_image_url(product_list[0])
            st.markdown(breadcrumb_list[0])
            st.text_area("New BC",key= 0)

        with col2:
            st.markdown(product_list[1])
            get_image_url(product_list[1])
            st.markdown(breadcrumb_list[1])
            st.text_input("New BC",key= 1)

        with col3:
            st.markdown(product_list[2])
            get_image_url(product_list[2])
            st.markdown(breadcrumb_list[2])
            st.text_input("New BC",key= 2)

        with col4:
            st.markdown(product_list[2])
            get_image_url(product_list[2])
            st.markdown(breadcrumb_list[2])
            st.text_input("New BC",key= 3)

if navigation == "Regex" : 

    st.header("Coucou")
