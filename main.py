import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.sidebar.title("Menu")
    # 4 buton
    page = st.sidebar.radio(
        "Select Page",
        ["Menu", "📊 Touch Parameter Visualization", "📊 User Parameter Visualization"]
    )

    # Sayfa içerikleri
    if page == "Menu":
        st.title("Touch and User Classification from Smart Fabric")
        st.write("""
        ### Project Description:
        This project focuses on classifying touch types and user identities based on sensor data collected from smart fabrics.
        Using Random Forest classifiers, the system predicts either the touch type or the user based on 3200 sensor features.
        The project also provides feature importance analysis and outlier detection to enhance data understanding.
        """)

    elif page == "📊 Touch Parameter Visualization":
        st.title("Touch Parameter - Feature Importances")
        st.write("Below is the Random Forest feature importance visualization for touch type classification.")
        st.image("kmeans_model_random_forest_touch.png", caption="Top 100 Features for Touch Prediction", use_container_width =True)

    elif page == "📊 User Parameter Visualization":
        st.title("User Parameter - Feature Importances")
        st.write("Below is the Random Forest feature importance visualization for user classification.")
        st.image("kmeans_model_random_forest_user.png", caption="Top 100 Features for User Prediction", use_container_width =True)

    
if __name__ == "__main__":
    main()
