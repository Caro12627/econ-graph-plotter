import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Supply and Demand Graph Plotter", layout="wide")

st.title("📈📉 Supply and Demand Graph Plotter")

#User input what shift
shift_type = st.radio(
    "Choose what type of shift you want to plot:",
    ["Demand only","Supply only","Both Demand and Supply"]
)

# Sliders for shifts
if shift_type == "Demand only":
    demand_shift = st.slider("Shift Demand Curve", -10,10,0)
    supply_shift = 0
elif shift_type == "Supply only":
    supply_shift = st.slider("Shift Supply Curve",-10,10,0)
    demand_shift = 0
#both
else:
    demand_shift = st.slider("Shift Demand Curve", -10,10,0)
    supply_shift = st.slider("Shift Supply Curve",-10,10,0)

# Price Values
p = np.linspace(0,30,100)

# Demand and Supply Functions
def demand(p):
    return 20 - 1 * p + demand_shift

def supply(p):
    return 5 + 1 * p + supply_shift

d_vals = demand(p) 
s_vals = supply(p)

# Find equilibrium approximately
diff = np.abs(d_vals - s_vals)
eq_index = np.argmin(diff)
eq_price = p[eq_index]
eq_quantity = d_vals[eq_index]

# Plotting using matplotlib
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_title("Supply and Demand Graph")
ax.plot(p, d_vals, label='Demand', color='blue')
ax.plot(p, s_vals, label='Supply', color='red')
ax.scatter(eq_price,eq_quantity, color = "green", s = 100, label = "Equilibrium")
ax.annotate("Equilibrium", (eq_price, eq_quantity), xytext=(eq_price + 1, eq_quantity),
            arrowprops=dict(arrowstyle="->"), fontsize = 9)

ax.set_xlabel("Price")
ax.set_ylabel("Quantity")
ax.legend()
ax.grid(True)

# Layouyt columns 
col1, col2 = st.columns([2,1])
with col1:
    st.pyplot(fig)

with col2: 
    st.subheader("Explanation")

    if demand_shift > 0 and supply_shift==0:
        st.write("Demand Increased -> shifted right -> Price and Quantity Increased -> Equilibrium Price and Quantity Increased")
    elif demand_shift < 0 and supply_shift==0:
        st.write("Demand Decreased -> shifted left -> Price and Quantity Decreased -> Equilibrium Price and Quantity Decreased")
    elif supply_shift > 0 and demand_shift==0:
        st.write("Supply Increased -> shifted right -> Price Decreased and Quantity Increased -> Equilibrium Price Decreased and Quantity Increased")
    elif supply_shift < 0 and demand_shift==0:
        st.write("Supply Decreased -> shifted left -> Price Increased and Quantity Decreased -> Equilibrium Price Increased and Quantity Decreased")
    elif demand_shift > 0 and supply_shift > 0:
        st.write("Demand Increased and Supply Increased -> Demand shifted right and Supply shifted right -> Price UNDETERMAINABLE and Quantity Increased -> Equilibrium Quantiy Increased and Price UNDETERMINABLE")
    elif demand_shift < 0 and supply_shift < 0:
        st.write("Demand Decreased and Supply Decreased -> Demand shifted left and Supply shifted left -> Price UNDETERMINABLE and Quantity Decreased -> Equilibrium Quantity Decreased and Price UNDETERMINABLE")
    elif demand_shift > 0 and supply_shift < 0:
        st.write("Demand Increased and Supply Decreased -> Demand shifted right and Supply shifted left -> Price Increased and Quantity UNDETERMINABLE -> Equilibrium Price Increased and Quantity UNDETERMINABLE")
    elif demand_shift < 0 and supply_shift > 0:
        st.write("Demand Decreased and Supply Increased -> Demand shifted left and Supply shifted right -> Price Decreased and Quantity UNDETERMINABLE -> Equilibrium Price Decreased and Quantity UNDETERMINABLE")
    else:
        st.write("No Shift in Demand or Supply -> No Change in Equilibrium Price or Quantity")
    
    st.write("Note: The equilibrium price and quantity are determined by the intersection of the demand and supply curves.")