import streamlit as st
from streamlit_echarts import st_echarts

nutritions_values = ['Calories', 'FatContent', 'SaturatedFatContent', 'CholesterolContent', 'SodiumContent', 'CarbohydrateContent', 'FiberContent', 'SugarContent', 'ProteinContent']

st.header('Meal Nutrition Analysis')
st.subheader('Choose your meal composition')

breakfast_recommendations=['Oats', 'Yoghurt with fruits', 'Egg', 'Nuts, seeds and low-fat diary', 'Banana and berries', 'Beans and lentils']
lunch_recommendations=['Dal', 'Vegetable curry', 'Brown rice', 'Fish', 'Green leafy vegetables', 'Chapathi']
dinner_recommendations=['Khichdi', 'Vegetable soup', 'Fish', 'Fruit salad', 'Buttermilk', 'Ragi dosa']

# Create select boxes for meal choices
breakfast_choice, lunch_choice, dinner_choice = st.columns(3)
breakfast_choice = st.selectbox('Choose your breakfast:', breakfast_recommendations)
lunch_choice = st.selectbox('Choose your lunch:', lunch_recommendations)
dinner_choice = st.selectbox('Choose your dinner:', dinner_recommendations)

choices=[breakfast_choice,lunch_choice,dinner_choice] 

# Calculating the sum of nutritional values of the choosen recipes
total_nutrition_values = {nutrition_value: 0 for nutrition_value in nutritions_values}
for choice, meals_ in zip(choices, [breakfast_recommendations, lunch_recommendations, dinner_recommendations]):
    for meal in meals_:
        if meal == choice:  # Check if the meal string matches the choice
            # For each nutritional value, add the value of the chosen meal to the total
            for nutrition_value in nutritions_values:
                total_nutrition_values[nutrition_value] += get_nutrition_value(meal, nutrition_value)

st.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Nutritional Values:</h5>', unsafe_allow_html=True)
nutritions_graph_options = {
"tooltip": {"trigger": "item"},
"legend": {"top": "5%", "left": "center"},
"series": [
{
    "name": "Nutritional Values",
    "type": "pie",
    "radius": ["40%", "70%"],
    "avoidLabelOverlap": False,
    "itemStyle": {
        "borderRadius": 10,
        "borderColor": "#fff",
        "borderWidth": 2,
    },
    "label": {"show": False, "position": "center"},
    "emphasis": {
        "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
    },
    "labelLine": {"show": False},
    "data": [{"value":round(total_nutrition_values[total_nutrition_value]),"name":total_nutrition_value} for total_nutrition_value in total_nutrition_values],
}
],
}       
st_echarts(options=nutritions_graph_options, height="500px",)