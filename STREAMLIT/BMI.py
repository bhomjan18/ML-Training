import streamlit as st

def calculate_bmi(weight, height, height_unit):
    if height_unit == "cm":
        bmi = weight / ((height / 100) ** 2)
    elif height_unit == "meter":
        bmi = weight / (height ** 2)
    elif height_unit == "feet":
        bmi = weight / ((height / 3.28) ** 2)
    elif height_unit == "inch":
        bmi = weight / ((height * 0.0254) ** 2)
    else:
        return None
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 16:
        return "Extreme Underweight", "https://as1.ftcdn.net/v2/jpg/05/77/39/66/1000_F_577396614_KTsFyZCHuPcehbIPk8QwGbcz3DqL64kH.jpg"
    elif 16 <= bmi < 18.5:
        return "Underweight", "https://newsmedia.tasnimnews.com/Tasnim/Uploaded/Image/1398/03/02/139803021453548717489974.jpg"
    elif 18.5 <= bmi < 25:
        return "Healthy", "https://martinswellness.com/media/wysiwyg/martins_blog_04242017_header_image.jpg"
    elif 25 <= bmi < 30:
        return "Overweight", "https://c8.alamy.com/comp/2R91B06/upset-male-overweight-cartoon-character-illustration-2R91B06.jpg"
    else:
        return "Extremely Overweight", "https://media.istockphoto.com/id/1490937583/vector/overweight-couple-cartoon-character.jpg?s=612x612&w=0&k=20&c=PdUcdlCPzUe9FRege_uNBK06C1PjWc7p5UmOOsEsQ3A="

st.title("BMI Calculator")

# Adding a brief description
st.write("Use this calculator to determine your BMI (Body Mass Index) based on your weight and height.")

weight = st.number_input("Enter weight (kg):", min_value=1.0, step=0.1)
height_unit = st.radio("Select height format:", ("cm", "inch", "feet", "meter"))
height = st.number_input("Enter height:", min_value=0.1, step=0.1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height, height_unit)
    if bmi:
        classification, image_url = classify_bmi(bmi)
        st.success(f"Your BMI index is {bmi}. Based on BMI: {classification}")
        
        # Displaying the image based on classification
        st.image(image_url, width=400, caption=f"BMI Classification: {classification}")
    else:
        st.error("Invalid height input. Please enter a valid height.")
