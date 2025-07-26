import streamlit as st
from streamlit_option_menu import option_menu
import time
import random



# st.title("Study capanion")
st.set_page_config(layout="wide")  # Ensures full-width navbar

# Create a top navigation bar
selected = option_menu(
    menu_title=None,  # No title
    options=[ "Home","About", "Contact", "Login","📂 Services"],
    icons=[ "info", "telephone", "person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",  # Ensures it appears at the top
    styles={
        "container": {"padding": "0!important", "background-color": "#333333"},
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {"color": "white", "font-size": "18px", "text-align": "center"},
        "nav-link-selected": {"background-color": "#f12454"},
    },
)

# if selected == "Home":
#     st.title("🏠 Home Page")
if selected == "About":
    st.title("ℹ️ About Page")
elif selected == "Contact":
    st.title("📞 Contact Page")
elif selected == "📂 topics":
    service_selected = option_menu(
        menu_title="Select a Topic",
        options=["Integers", "Geometry", "Fractions","Algebra","Quiz"],
        icons=["search", "brush", "code"],
        menu_icon="tools",
        default_index=0,
        orientation="vertical",
    )
    
    if service_selected == "Integers":
        st.title("Integers")
        st.write("Learn about different types of integers and how to work with them!")
        with st.expander("1. What are Integers?"):
            st.write("""
            - Integers include **positive numbers, negative numbers, and zero** (e.g., -3, -2, -1, 0, 1, 2, 3).
            - Positive integers are greater than zero (e.g., 1, 2, 3, …).
            - Negative integers are less than zero (e.g., -1, -2, -3, …).
            - Zero (0) is **neither positive nor negative**.
            """)

        with st.expander("2. Representing Integers"):
            st.write("""
            - **Number Line**: Integers are represented on a number line, with negatives on the left and positives on the right.
            - **Comparing Integers**:
                - Numbers to the right are greater.
                - Numbers to the left are smaller.
                - Example: -5 is smaller than -2 because -5 is further left.
            """)

        with st.expander("3. Operations with Integers"):
            st.subheader("a) Addition of Integers")
            st.write("""
            - **Same Sign**: Add absolute values, keep the sign.
                - Example: (-3) + (-5) = -8
            - **Different Sign**: Subtract absolute values, take the sign of the bigger number.
                - Example: 7 + (-4) = 3
            """)

            st.subheader("b) Subtraction of Integers")
            st.write("""
            - Change subtraction into addition by **adding the opposite**.
                - Example: 6 - (-2) = 6 + 2 = 8
                - Example: (-3) - 5 = (-3) + (-5) = -8
            """)

            st.subheader("c) Multiplication and Division of Integers")
            st.write("""
            - **Same Signs**: Positive result
                - Example: (-4) × (-3) = 12
            - **Different Signs**: Negative result
                - Example: (-6) × (2) = -12
            """)

        with st.expander("4. Absolute Value"):
            st.write("""
            - The absolute value of a number is its distance from zero (always positive).
                - Example: | -4 | = 4
            """)

        with st.expander("5. Real-Life Applications of Integers"):
            st.write("""
            - **Temperature**: -5°C (cold) vs. 10°C (warm).
            - **Bank Transactions**: +$20 (deposit), -$10 (withdrawal).
            - **Elevation**: 200m above sea level (+200), 50m below sea level (-50).
            """)

        pass
    elif service_selected == "Geometry":
        st.title("Geometry")
        st.write("Learn about different geometry and how to work with them!")
        with st.expander("1. Basic Geometry Terms"):
            st.write("**Point** – A location in space (no size).")
            st.write("**Line** – Extends infinitely in both directions.")
            st.write("**Line Segment** – A part of a line with two endpoints.")
            st.write("**Ray** – A part of a line that starts at one point and goes on forever in one direction.")
            st.write("**Angle** – Formed when two rays share a common endpoint.")
        
        with st.expander("2. Types of Angles"):
            st.write("**Acute Angle** – Less than 90°")
            st.write("**Right Angle** – Exactly 90°")
            st.write("**Obtuse Angle** – More than 90° but less than 180°")
            st.write("**Straight Angle** – Exactly 180°")
        
        with st.expander("3. Types of Triangles"):
            st.subheader("By Sides:")
            st.write("**Equilateral Triangle** – All sides are equal.")
            st.write("**Isosceles Triangle** – Two sides are equal.")
            st.write("**Scalene Triangle** – All sides are different.")
            
            st.subheader("By Angles:")
            st.write("**Acute Triangle** – All angles are less than 90°.")
            st.write("**Right Triangle** – Has one right angle (90°).")
            st.write("**Obtuse Triangle** – Has one obtuse angle (more than 90° but less than 180°).")
        pass
    elif service_selected == "Fractions":
        st.title("Fractions")
        st.write("Learn about different types of fractions and how to work with them!")
        
        with st.expander("1. Types of Fractions"):
            st.write("- **Proper Fractions**: Numerator is smaller than denominator (e.g., 3/4, 2/5).")
            st.write("- **Improper Fractions**: Numerator is greater than or equal to denominator (e.g., 7/4, 9/5).")
            st.write("- **Mixed Numbers**: Whole number and a fraction combined (e.g., 2 ½, 3 ¾).")
        
        with st.expander("2. Comparing and Ordering Fractions"):
            st.write("- Find a **common denominator** to compare fractions.")
            st.write("- Convert fractions to **decimals** for easier comparison.")
        
        with st.expander("3. Simplifying (Reducing) Fractions"):
            st.write("- Divide numerator and denominator by their **Greatest Common Factor (GCF)**.")
            st.write("- Example: **12/18** → GCF = 6, so (12 ÷ 6) / (18 ÷ 6) = **2/3**.")
        
        with st.expander("4. Converting Fractions"):
            st.write("- **Improper to Mixed Number**: Divide numerator by denominator.")
            st.write("  - Example: **7/3** = **2 1/3**.")
            st.write("- **Mixed Number to Improper**: Multiply whole number by denominator and add numerator.")
            st.write("  - Example: **2 1/3** → (2 × 3) + 1 = **7/3**.")
        
        with st.expander("5. Adding and Subtracting Fractions"):
            st.write("- **Same denominator**: Add/subtract numerators.")
            st.write("- **Different denominators**: Find **common denominator** before adding/subtracting.")
            st.write("  - Example: **1/4 + 2/3**")
            st.write("  - LCD of 4 and 3 is **12**. Convert: **1/4 = 3/12, 2/3 = 8/12**.")
            st.write("  - **3/12 + 8/12 = 11/12**.")
        
        with st.expander("6. Multiplying and Dividing Fractions"):
            st.write("- **Multiplication**: Multiply numerators and denominators.")
            st.write("  - Example: **2/3 × 4/5 = (2×4)/(3×5) = 8/15**.")
            st.write("- **Division**: Flip (reciprocal) the second fraction and multiply.")
            st.write("  - Example: **2/3 ÷ 4/5 = 2/3 × 5/4 = (2×5)/(3×4) = 10/12 = 5/6**.")
        
        with st.expander("7. Word Problems Involving Fractions"):
            st.write("- Solve real-life problems using fractions in cooking, measuring, and sharing.")
        pass
    elif service_selected == "Algebra":
        st.title("Algebra")
        st.write("Learn about Algebra and how to work with them!")

        with st.expander("1️⃣ Understanding Variables and Expressions"):
            st.write("- A **variable** is a letter or symbol that represents an unknown number (e.g., x, y, z).")
            st.write("- An **expression** contains numbers, variables, and operations (e.g., 3x + 5).")
            if st.checkbox("Example: Evaluate 3x + 5 for x = 2"):
                x = 2
                result = 3 * x + 5
                st.write(f"3(2) + 5 = {result}")
        
        with st.expander("2️⃣ Order of Operations (PEMDAS)"):
            st.write("- Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right)")
            if st.checkbox("Example: Calculate 5 + 3 × (2 + 4)² ÷ 6"):
                result = 5 + 3 * (2 + 4) ** 2 / 6
                st.write(f"Result: {result}")
    
        with st.expander("3️⃣ Writing and Simplifying Expressions"):
            st.write("- **Combining like terms** (e.g., 3x + 4x = 7x)")
            st.write("- **Distributive property**: 3(2x + 4) = 6x + 12")
        
        with st.expander("4️⃣ Solving Simple Equations"):
            st.write("- Example: Solve for x in 3x + 4 = 16")
            if st.checkbox("Show Solution"):
                x = (16 - 4) / 3
                st.write(f"Solution: x = {x}")
        
        with st.expander("5️⃣ Inequalities"):
            st.write("- Symbols: <, >, ≤, ≥")
            st.write("- Example: x + 3 > 7 → x > 4")
        
        with st.expander("6️⃣ Coordinate Plane & Graphing"):
            st.write("- Ordered pairs (x, y)")
            st.write("- Plotting points and graphing simple equations")
        
        with st.expander("7️⃣ Word Problems"):
            st.write("Example: 'Three times a number increased by five is fourteen.' → 3x + 5 = 14")
    elif service_selected == "Quiz":
        with st.expander("Quiz - algebra"):
            st.write("Test your knowledge with these questions!")
            q1 = st.radio("1. What is the value of x in the equation 2x + 3 = 11?", ["x = 3", "x = 4", "x = 5"],index=None)
            q2 = st.radio("2. Simplify: 5x + 3x - 2x", ["6x", "8x", "10x"],index=None)
            q3 = st.radio("3. What is the result of (3 + 2) × 4?", ["20", "14", "24"],index=None)

            if st.button("Submit answers"):
                score = 0
                if q1 == "x = 4":
                    # st.success("Correct!")
                    score +=1
                # elif q1:
                #     st.error("Try again.")
                
                
                if q2 == "6x":
                    # st.success("Correct!")
                    score+=1
                # elif q2:
                #     st.error("Try again.")
                
                if q3 == "20":
                    # st.success("Correct!")
                    score+=1
                # elif q3:
                #     st.error("Try again.")
                st.write(f"Your score: {score}/3")
        with st.expander("Quiz - integers"):
            st.write("Test your knowledge with this quick quiz!")
            q1 = st.radio("What is the absolute value of -7?", ["-7", "7", "0", "-1"],index=None)
            q2 = st.radio("Which is greater: -3 or -5?", ["-3", "-5"],index=None)
            q3 = st.radio("What is (-2) + 5?", ["-3", "3", "7", "-7"],index=None)
            
            if st.button("Submit Answers"):
                score = 0
                if q1 == "7":
                    score += 1
                # elif 
                if q2 == "-3":
                    score += 1
                if q3 == "3":
                    score += 1
                st.write(f"Your score: {score}/3")

        with st.expander("Quiz - Geometry"):
            score = 0
            
            question1 = st.radio("1. What is a triangle with all sides equal called?", ["Scalene Triangle", "Isosceles Triangle", "Equilateral Triangle"], key="q1",index=None)
            question2 = st.radio("2. What is an angle exactly 90° called?", ["Acute Angle", "Right Angle", "Obtuse Angle"], key="q2",index=None)
            question3 = st.radio("3. What do you call a line segment that joins two points on a circle?", ["Radius", "Chord", "Diameter"], key="q3",index=None)
            
            if st.button("Submit Answer"):
                if question1 == "Equilateral Triangle":
                    score += 1
                if question2 == "Right Angle":
                    score += 1
                if question3 == "Chord":
                    score += 1
                
                st.write(f"Your score: {score}/3")

        with st.expander("Quiz - Fractions"):
            q1 = st.radio("1. What type of fraction is 7/4?", ["Proper Fraction", "Improper Fraction", "Mixed Number"],index=None)
            q2 = st.radio("2. What is 2 1/2 as an improper fraction?", ["5/2", "3/2", "4/3"],index=None)
            q3 = st.radio("3. What is 1/4 + 2/3?", ["3/7", "8/12", "11/12"],index=None)
            
            if st.button("Submit"):
                score = 0
                wrong = []
                if q1 == "Improper Fraction":
                    score += 1
                elif q1:
                    wrong.append("Question 1")

                if q2 == "5/2":
                    score += 1
                elif q2:
                    wrong.append("Question 2")

                if q3 == "11/12":
                    score += 1
                elif q3:
                    wrong.append("Question 3")
                
                if score == 3 :
                    st.write(f"Your score: {score}/3 with none wrong")
                else:
                    st.write(f"your score: {score}/3 with {wrong} wrong")

elif selected == "Login":
    st.header("welcome to the math app")
    st.text("Fill in this form to personalise your learning experience")

    first,last = st.columns(2)


    f = first.text_input('First Name')
    l = last.text_input('Last Name')



    email,mob = st.columns([3,1])

    e = email.text_input('Email ID')
    m = mob.text_input('Mob Number')


    user,pw,pw2 = st.columns(3)

    u = user.text_input('Username')
    p1 = pw.text_input('Password',type = 'password')
    p2 = pw2.text_input('retype your Password',type = 'password')


    ch,bl,sub = st.columns(3)

    c = ch.checkbox('I Agree')
    if p1 == p2:
        if sub.button('submit'):
            st.success('submited!')

            info = {
                'fname':f,
                'lname':l,
                'email':e,
                'mobile':m,
                'username':u,
                'password':p1,
                'T&C':c
            }
            st.table(info)  

            b,con,b = st.columns(3)
            if con.button('confirm'):
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.1)
                    progress.progress(i+1)

            
                st.success('confirmed')
    else:
        st.error("pasword doesnt match")


if selected == "Home":

    st.subheader("welcome to my math app")

    



