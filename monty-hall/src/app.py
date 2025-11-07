import streamlit as st

from src.monty_hall import montyhall, simulate

st.title("Monty Hall Problem Simulation")
num_simulations = st.number_input("Number of Simulations",
                                   min_value=100, max_value=100000,
                                   value=10000, step=1000)

col1, col2 = st.columns(2)
col1.header("Switching Strategy")
col2.header("Staying Strategy")
chart1 = col1.line_chart(x = None,y = None,height=400)
chart2 = col2.line_chart(x = None,y = None,height=400)
switch_win_count = 0
stay_win_count = 0
if st.button("Run Simulation"):
    for i in range(num_simulations):
            switch_win_rate = simulate(True,1)
            if switch_win_rate:
                  switch_win_count += 1
                  chart1.add_rows({'Switch Win Rate': [switch_win_count / (i + 1)]})

            stay_win_rate = simulate(False,1)
            if stay_win_rate:
                  stay_win_count += 1
                  chart2.add_rows({'Stay Win Rate': [stay_win_count / (i + 1)]})

    st.write(f"After {num_simulations} simulations:")
    st.write(f"- Win rate when switching: {switch_win_count / (i + 1):.2f}")
    st.write(f"- Win rate when staying: {stay_win_count / (i + 1):.2f}")


