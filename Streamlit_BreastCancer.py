import streamlit as st
import requests

st.title("Breast Cancer Detection App")


def get_predictions(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst,
texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst):
    url = f"https://breast-cancer-detection-system.herokuapp.com/predict?radius_mean={radius_mean}&texture_mean={texture_mean}&perimeter_mean={perimeter_mean}&area_mean={area_mean}&smoothness_mean={smoothness_mean}&compactness_mean={compactness_mean}&concavity_mean={concavity_mean}&concave_points_mean={concave_points_mean}&symmetry_mean={symmetry_mean}&fractal_dimension_mean={fractal_dimension_mean}&radius_se={radius_se}&texture_se={texture_se}&perimeter_se={perimeter_se}&area_se={area_se}&smoothness_se={smoothness_se}&compactness_se={compactness_se}&concavity_se={concavity_se}&concave_points_se={concave_points_se}&symmetry_se={symmetry_se}&fractal_dimension_se={fractal_dimension_se}&radius_worst={radius_worst}&texture_worst={texture_worst}&perimeter_worst={perimeter_worst}&area_worst={area_worst}&smoothness_worst={smoothness_worst}&compactness_worst={compactness_worst}&concavity_worst={concavity_worst}&concave_points_worst={concave_points_worst}&symmetry_worst={symmetry_worst}&fractal_dimension_worst={fractal_dimension_worst}"
    response = requests.post(url)
    json_response = response.json()
    diagnosis = json_response["prediction"]
    return diagnosis


radius_mean = st.number_input("Enter radius mean")
texture_mean = st.number_input("Enter texture mean")
perimeter_mean = st.number_input("Enter perimeter mean")
area_mean = st.number_input("Enter area mean")
smoothness_mean = st.number_input("Enter smoothness mean")
compactness_mean = st.number_input("Enter compactness mean")
concavity_mean = st.number_input("Enter concavity mean")
concave_points_mean = st.number_input("Enter concave points mean")
symmetry_mean = st.number_input("Enter symmetry mean")
fractal_dimension_mean = st.number_input("Enter fractal dimension mean")
radius_se = st.number_input("Enter radius se")
texture_se = st.number_input("Enter texture se")
perimeter_se = st.number_input("Enter perimeter se")
area_se = st.number_input("Enter area se")
smoothness_se = st.number_input("Enter smoothness se")
compactness_se = st.number_input("Enter compactness se")
concavity_se = st.number_input("Enter concavity se")
concave_points_se = st.number_input("Enter concave points se")
symmetry_se = st.number_input("Enter symmetry se")
fractal_dimension_se = st.number_input("Enter fractal dimension se")
radius_worst = st.number_input("Enter radius worst")
texture_worst = st.number_input("Enter texture worst")
perimeter_worst = st.number_input("Enter perimeter worst")
area_worst = st.number_input("Enter area worst")
smoothness_worst = st.number_input("Enter smoothness worst")
compactness_worst = st.number_input("Enter compactness worst")
concavity_worst = st.number_input("Enter concavity worst")
concave_points_worst = st.number_input("Enter concave points worst")
symmetry_worst = st.number_input("Enter symmetry worst")
fractal_dimension_worst = st.number_input("Enter fractal dimension worst")

result = ""

# when 'Predict' is clicked, make the prediction and store it

if st.button("Predict"):
    result = get_predictions(radius_mean=radius_mean, texture_mean=texture_mean, perimeter_mean=perimeter_mean,
                             area_mean=area_mean, smoothness_mean=smoothness_mean, compactness_mean=compactness_mean,
                             concavity_mean=concavity_mean, concave_points_mean=concave_points_mean,
                             symmetry_mean=symmetry_mean, fractal_dimension_mean=fractal_dimension_mean,
                             radius_se=radius_se, texture_se=texture_se, perimeter_se=perimeter_se, area_se=area_se,
                             smoothness_se=smoothness_se, compactness_se=compactness_se, concavity_se=concavity_se,
                             concave_points_se=concave_points_se, symmetry_se=symmetry_se,
                             fractal_dimension_se=fractal_dimension_se, radius_worst=radius_worst,
                             texture_worst=texture_worst, perimeter_worst=perimeter_worst, area_worst=area_worst,
                             smoothness_worst=smoothness_worst, compactness_worst=compactness_worst,
                             concavity_worst=concavity_worst, concave_points_worst=concave_points_worst,
                             symmetry_worst=symmetry_worst, fractal_dimension_worst=fractal_dimension_worst)
    st.success(f"Breast Cancer  {result}")
