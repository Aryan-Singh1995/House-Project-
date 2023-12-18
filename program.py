
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os
import altair as alt
house: object = pickle.load(open('data.pkl', 'rb'))
data: object = pickle.load(open('tune (1).pkl', 'rb'))

Pipe1 = pickle.load(open('pipeline.pkl', 'rb'))

sidebar_option = st.sidebar.selectbox("Select an Option", ["Predictor", "Recommender","Dashboard"])

if sidebar_option == "Predictor":
    st.header("Prediction Section")
    st.title('HOUSE_PRICE_PREDICTOR')
    st.image('R.jfif')

    property_type = st.selectbox('PROPERTY', house['property_type'].unique())
    floorNum = st.selectbox('floorNum', house['floorNum'].unique())
    agePossession = st.selectbox('agePossession', house['agePossession'].unique())
    luxury_score = st.selectbox('luxury_score', house['luxury_score'].unique())
    Furnished = st.selectbox('Furnished', house['Furnished'].unique())

    price_per_sqft = st.selectbox('price_per_sqft', house['price_per_sqft'].unique())
    bedRoom = st.selectbox('bedRoom', house['bedRoom'].unique())
    bathroom = st.selectbox('bathroom', house['bathroom'].unique())
    balcony = st.selectbox('balcony', house['balcony'].unique())
    BHK = st.selectbox('BHK', house['BHK'].unique())

    Store = st.selectbox('Store', ['Yes','No'])
    Build = st.selectbox('Build', house['Build'])

    if st.button('Prtedict Price'):


        if Store == 'Yes':
            Store = 1
        else:
            Store = 0




        query_data = {
            'property_type': property_type,
            'price_per_sqft': price_per_sqft,
            'bedRoom': bedRoom,
            'bathroom': bathroom,
            'balcony': balcony,
            'floorNum': floorNum,
            'agePossession': agePossession,
            'BHK': BHK,
            'Store': Store,
            'luxury_score': luxury_score,
            'Furnished': Furnished,
            'Build': Build
        }

        # Convert the dictionary to a pandas DataFrame
        query_df = pd.DataFrame([query_data])

        prediction = round(Pipe1.predict(query_df).item())

        # Display the rounded prediction as a title
        st.title(f"Property Price is: {prediction}")









elif sidebar_option == "Recommender":
    st.header("Property_Recommender")
    Location = st.selectbox( 'Location', data['Location'].unique() )

    if st.button( 'Recommend' ):
        def final1(Location):
            return data[data['Location'] == Location]


        input_location = Location
        result = st.dataframe(final1(input_location))

        print(result)



elif sidebar_option == "Dashboard":


    tab, tab0, tab1, tab2, tab3, tab4 = st.tabs(['Main','Number of Flat_&_House','price', 'Furnished', 'BHK','other_information'])

    with tab:
        st.header('House Dataset')
        st.write(house)
    with tab1:
        st.header('Price Range')

        st.line_chart(data, y='price')

    with tab0:
        st.header('FLat vs House')
        st.bar_chart(house["property_type"].value_counts())

    with tab2:
        st.header('Furnished or Not')
        st.bar_chart(house["Furnished"].value_counts())


    with tab3:
        st.header('BHK')
        st.bar_chart(house["BHK"].value_counts())

    with tab4:
        st.header('luxury_score Analysis ')

        st.bar_chart( house["luxury_score"].value_counts() )

        st.header( 'bedRoom Analysis ' )

        st.bar_chart( house["bedRoom"].value_counts() )

        st.header( 'balcony Analysis ' )

        st.bar_chart( house["balcony"].value_counts() )

        st.header( 'floorNum Analysis ' )

        st.bar_chart( house["floorNum"].value_counts() )

        st.header( 'agePossession Analysis ' )

        st.bar_chart( house["agePossession"].value_counts() )

        st.header( 'price_per_sqft Analysis ' )

        st.line_chart( house, y="price_per_sqft")



























