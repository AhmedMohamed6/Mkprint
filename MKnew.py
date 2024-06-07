import streamlit as st

st.set_page_config(page_title='MK Print', page_icon=':art:', layout='wide')

def login():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        valid_users = {"ahmed": "26468463", "tarek": "tarek", "youssef": "youssef", "mohamed": "mohamed"}

        if username in valid_users and password == valid_users[username]:
            st.success("Login Successful!")
            st.balloons()
            st.session_state.logged_in = True
        else:
            st.error("Invalid Username or Password")

def home():
    
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 20vh; color: #3498db; font-family: 'Arial', sans-serif;">
            <h1 style="text-align: center;">MK Print</h1>
        </div>
                """, unsafe_allow_html=True)

    
    st.header("Calculator  :bulb:")
        
    size_width = st.number_input('Enter the width (in cm): :straight_ruler:', key='width')
    size_height = st.number_input('Enter the height (in cm): :straight_ruler:', key='height')
    pieces = st.number_input('Enter the pieces : ', key='pieces')

    if st.button("Calculate"):
    # ------------------Print Way Price---------------------

                
    # ------------------Print Way Price---------------------
        
        Print_way_Price = 230
    
        width_result_Print_way = int((102 / (size_width + 0.3)))
        height_result_Print_way = int((85 / (size_height + 0.3)))
        result_meter_Print_way = width_result_Print_way * height_result_Print_way
        
        industrial_cost_Print_way = float((pieces / width_result_Print_way) * (size_height + 0.3))
        industrial_cost_Print_way_2 = int(1.07*(industrial_cost_Print_way/100)*180)
        price_of_work_Print_way = int(1.07*(industrial_cost_Print_way/100)*235)
        sales_cost = (price_of_work_Print_way *0.5)+price_of_work_Print_way
        cutter_profit = price_of_work_Print_way - industrial_cost_Print_way_2
       # profit_Print_way = (price_of_work_Print_way *0.5)+price_of_work_Print_way
        st.write('------------------Screen color------------------')
        st.write(f'For a shape of size {size_width} cm')
        st.write(f'There are approximately {width_result_Print_way} pieces in width lines in one meter.')
    
        st.write(f'For a shape of size {size_height} cm')
        st.write(f'There are approximately {height_result_Print_way} pieces in width lines in one meter.')
    
        st.write(f'For a shape of size {size_width} cm x {size_height} cm')
        
        st.write(f'Meter has approximately {result_meter_Print_way} shape.')
        
        st.write(f'For a shape of size {industrial_cost_Print_way} cm')
        
        st.write(f'Industrial cost {industrial_cost_Print_way_2}EGP.') 
    
        st.write(f'Price of work {price_of_work_Print_way}EGP.')

        st.write(f'Cutter profit {cutter_profit}EGP.') 

       # st.write(f'Profit {profit_Print_way}EGP.')  


def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        home()
    else:
        login()

if __name__ == "__main__":
    main()
