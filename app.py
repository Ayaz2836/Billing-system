import streamlit as st
import json
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Grocery Store Manager",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }
    
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
        animation: fadeIn 1s ease-in;
        margin-bottom: 2rem;
    }
    
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        animation: fadeIn 0.8s ease-in;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .success-message {
        padding: 1rem;
        background: #d4edda;
        border-left: 4px solid #28a745;
        border-radius: 5px;
        animation: slideIn 0.5s ease-out;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'store' not in st.session_state:
    st.session_state.store = {
        "biscuit": {
            "sooper": [10, 20, 30, 40],
            "up": [10, 20, 40, 30],
            "peanut": [5, 10, 20, 40]
        },
        "nimko": {
            "crunch": [5, 10, 20, 30],
            "salva": [10, 20, 30, 40],
            "darbari tikka": [10, 20, 40, 50]
        }
    }

if 'cart' not in st.session_state:
    st.session_state.cart = []

if 'customer_name' not in st.session_state:
    st.session_state.customer_name = ""

# Header
st.markdown('<div class="main-header"><h1>🛒 Grocery Store Manager</h1><p>Manage your store inventory and generate bills</p></div>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📋 Navigation")
page = st.sidebar.radio("Select Page", ["🏠 Home", "💰 Generate Bill", "📊 Rate List", "➕ Add Items", "🗑️ Remove Items"])

# Home Page
if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Total Categories", len(st.session_state.store))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        total_items = sum(len(items) for items in st.session_state.store.values())
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Total Products", total_items)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Cart Items", len(st.session_state.cart))
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📦 Current Inventory")
    
    for category, items in st.session_state.store.items():
        with st.expander(f"📁 {category.upper()}", expanded=False):
            for item, prices in items.items():
                st.write(f"**{item}**: {prices}")

# Generate Bill Page
elif page == "💰 Generate Bill":
    st.header("💰 Generate Customer Bill")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.session_state.customer_name = st.text_input("👤 Customer Name", st.session_state.customer_name)
        
        st.subheader("🛍️ Add Items to Cart")
        
        category = st.selectbox("Select Category", list(st.session_state.store.keys()))
        
        if category:
            item = st.selectbox("Select Item", list(st.session_state.store[category].keys()))
            
            if item:
                prices = st.session_state.store[category][item]
                price_options = [f"Size {i+1}: ${price}" for i, price in enumerate(prices)]
                selected_price_idx = st.selectbox("Select Size/Price", range(len(prices)), format_func=lambda x: price_options[x])
                
                quantity = st.number_input("Quantity", min_value=1, value=1)
                
                if st.button("➕ Add to Cart", use_container_width=True):
                    price = prices[selected_price_idx]
                    total_price = price * quantity
                    st.session_state.cart.append({
                        "item": item,
                        "category": category,
                        "price": price,
                        "quantity": quantity,
                        "total": total_price
                    })
                    st.success(f"✅ Added {quantity}x {item} to cart!")
                    time.sleep(0.5)
                    st.rerun()
    
    with col2:
        st.subheader("🛒 Shopping Cart")
        
        if st.session_state.cart:
            total_bill = 0
            for idx, cart_item in enumerate(st.session_state.cart):
                st.markdown(f"""
                <div class="card">
                    <strong>{cart_item['item']}</strong><br>
                    Qty: {cart_item['quantity']} × ${cart_item['price']} = ${cart_item['total']}
                </div>
                """, unsafe_allow_html=True)
                total_bill += cart_item['total']
                
                if st.button(f"🗑️ Remove", key=f"remove_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()
            
            st.markdown("---")
            st.markdown(f"### 💵 Total: ${total_bill}")
            
            if st.button("🧾 Generate Bill", use_container_width=True):
                if st.session_state.customer_name:
                    st.balloons()
                    st.markdown(f"""
                    <div class="success-message">
                        <h3>✅ Bill Generated Successfully!</h3>
                        <p><strong>Customer:</strong> {st.session_state.customer_name}</p>
                        <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                        <p><strong>Total Amount:</strong> ${total_bill}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Clear cart after bill generation
                    if st.button("🔄 New Transaction"):
                        st.session_state.cart = []
                        st.session_state.customer_name = ""
                        st.rerun()
                else:
                    st.error("⚠️ Please enter customer name!")
        else:
            st.info("Cart is empty. Add items to generate a bill.")

# Rate List Page
elif page == "📊 Rate List":
    st.header("📊 Product Rate List")
    
    for category, items in st.session_state.store.items():
        st.subheader(f"📁 {category.upper()}")
        
        data = []
        for item, prices in items.items():
            for idx, price in enumerate(prices):
                data.append({
                    "Item": item,
                    "Size": f"Size {idx + 1}",
                    "Price": f"${price}"
                })
        
        st.table(data)
        st.markdown("---")

# Add Items Page
elif page == "➕ Add Items":
    st.header("➕ Add New Items")
    
    tab1, tab2 = st.tabs(["Add to Existing Category", "Create New Category"])
    
    with tab1:
        category = st.selectbox("Select Category", list(st.session_state.store.keys()), key="add_existing")
        item_name = st.text_input("Item Name")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            price1 = st.number_input("Price 1", min_value=0, value=10)
        with col2:
            price2 = st.number_input("Price 2", min_value=0, value=20)
        with col3:
            price3 = st.number_input("Price 3", min_value=0, value=30)
        with col4:
            price4 = st.number_input("Price 4", min_value=0, value=40)
        
        if st.button("➕ Add Item", use_container_width=True):
            if item_name:
                st.session_state.store[category][item_name] = [price1, price2, price3, price4]
                st.success(f"✅ Added {item_name} to {category}!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("⚠️ Please enter item name!")
    
    with tab2:
        new_category = st.text_input("New Category Name")
        new_item = st.text_input("First Item Name")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            p1 = st.number_input("Price 1", min_value=0, value=10, key="new_p1")
        with col2:
            p2 = st.number_input("Price 2", min_value=0, value=20, key="new_p2")
        with col3:
            p3 = st.number_input("Price 3", min_value=0, value=30, key="new_p3")
        with col4:
            p4 = st.number_input("Price 4", min_value=0, value=40, key="new_p4")
        
        if st.button("➕ Create Category", use_container_width=True):
            if new_category and new_item:
                st.session_state.store[new_category] = {new_item: [p1, p2, p3, p4]}
                st.success(f"✅ Created new category: {new_category}!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("⚠️ Please enter both category and item name!")

# Remove Items Page
elif page == "🗑️ Remove Items":
    st.header("🗑️ Remove Items")
    
    tab1, tab2 = st.tabs(["Remove Item", "Remove Category"])
    
    with tab1:
        category = st.selectbox("Select Category", list(st.session_state.store.keys()), key="remove_item_cat")
        
        if category and st.session_state.store[category]:
            item = st.selectbox("Select Item to Remove", list(st.session_state.store[category].keys()))
            
            if st.button("🗑️ Remove Item", use_container_width=True):
                del st.session_state.store[category][item]
                st.success(f"✅ Removed {item} from {category}!")
                time.sleep(1)
                st.rerun()
        else:
            st.info("No items in this category")
    
    with tab2:
        category_to_remove = st.selectbox("Select Category to Remove", list(st.session_state.store.keys()), key="remove_cat")
        
        st.warning(f"⚠️ This will remove the entire '{category_to_remove}' category and all its items!")
        
        if st.button("🗑️ Remove Category", use_container_width=True):
            del st.session_state.store[category_to_remove]
            st.success(f"✅ Removed category: {category_to_remove}!")
            time.sleep(1)
            st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
