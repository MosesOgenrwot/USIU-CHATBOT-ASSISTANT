"""
Streamlit Frontend for USIU-Africa Student Support Chatbot
Clean, user-friendly interface
"""

import streamlit as st
import requests
import time
from typing import Dict, Any

# Page configuration
st.set_page_config(
    page_title="USIU-Africa Student Support",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# API Configuration
API_URL = "http://localhost:8000"

# Custom CSS for better appearance
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        border-radius: 0.25rem;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        background-color: #d1ecf1;
        border-left: 4px solid #0c5460;
        border-radius: 0.25rem;
        margin: 1rem 0;
    }
    .category-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background-color: #007bff;
        color: white;
        border-radius: 1rem;
        font-size: 0.85rem;
        margin: 0.25rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_status" not in st.session_state:
    st.session_state.api_status = "unknown"

# Header
st.title("🎓 USIU-Africa Student Support")
st.caption("Multi-Agent AI Assistant powered by specialized knowledge agents")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This chatbot uses a **multi-agent system** with specialized agents for:
    
    - 💰 **Fees & Finance**
    - 📚 **Academic Programs**
    - 🏛️ **Campus Facilities**
    - 🤝 **Student Services**
    - 📋 **Conduct & Policies**
    """)
    
    st.divider()
    
    # API Status Check
    if st.button("🔄 Check API Status"):
        try:
            response = requests.get(f"{API_URL}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                st.session_state.api_status = "online"
                st.success("✅ API is online")
                with st.expander("API Details"):
                    st.json(data)
            else:
                st.session_state.api_status = "error"
                st.error("❌ API returned an error")
        except Exception as e:
            st.session_state.api_status = "offline"
            st.error(f"❌ Cannot connect to API\n\n{str(e)}")
    
    st.divider()
    
    # Example queries
    st.subheader("💡 Try asking:")
    example_queries = [
        "What are the fees for nursing?",
        "How do I pay via M-Pesa?",
        "What is the minimum GPA required?",
        "Where is the library?",
        "What are the library hours?",
        "Tell me about scholarships",
        "What are the rules about alcohol?",
        "How do I contact the finance office?"
    ]
    
    for query in example_queries:
        if st.button(query, key=f"example_{query}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": query})
            st.rerun()
    
    st.divider()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Display category badge for assistant messages
        if message["role"] == "assistant" and "metadata" in message:
            category = message["metadata"].get("category", "general")
            st.markdown(
                f'<span class="category-badge">📂 {category.replace("_", " ").title()}</span>',
                unsafe_allow_html=True
            )

# Chat input
user_input = st.chat_input("Ask me anything about USIU-Africa...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                # Call API
                response = requests.post(
                    f"{API_URL}/chat",
                    json={"question": user_input},
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data["answer"]
                    category = data.get("category", "general")
                    sources = data.get("sources", [])
                    
                    # Display answer
                    st.markdown(answer)
                    
                    # Display metadata
                    st.markdown(
                        f'<span class="category-badge">📂 {category.replace("_", " ").title()}</span>',
                        unsafe_allow_html=True
                    )
                    
                    # Show sources if available
                    if sources:
                        with st.expander("📚 Knowledge Sources"):
                            for source in sources:
                                st.write(f"- {source}")
                    
                    # Save assistant message with metadata
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "metadata": {
                            "category": category,
                            "sources": sources
                        }
                    })
                    
                    # Feedback buttons
                    col1, col2, col3 = st.columns([1, 1, 4])
                    with col1:
                        if st.button("👍", key=f"thumbs_up_{len(st.session_state.messages)}"):
                            st.toast("Thanks for your feedback!")
                    with col2:
                        if st.button("👎", key=f"thumbs_down_{len(st.session_state.messages)}"):
                            st.toast("We'll work on improving!")
                
                elif response.status_code == 500:
                    error_msg = "⚠️ The server encountered an error. Please try again or rephrase your question."
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
                else:
                    error_msg = f"⚠️ Unexpected response from server (Status: {response.status_code})"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
            
            except requests.exceptions.ConnectionError:
                error_msg = """
                ❌ **Cannot connect to the backend API**
                
                Please make sure:
                1. The backend server is running (`uvicorn backend.api:app --reload`)
                2. The API is accessible at http://localhost:8000
                3. No firewall is blocking the connection
                
                To start the backend, run:
                ```bash
                uvicorn backend.api:app --reload
                ```
                """
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "❌ Backend API is not available. Please start the server."
                })
            
            except requests.exceptions.Timeout:
                error_msg = "⏱️ The request timed out. The server might be overloaded. Please try again."
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
            
            except Exception as e:
                error_msg = f"❌ An error occurred: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })

# Footer
st.divider()
st.caption("""
**USIU-Africa Contact Information:**
           
- 📧 Email: admit@usiu.ac.ke
- 📞 Phone: +254 730 116 290/291
- 🌐 Website: www.usiu.ac.ke
- 🏫 Portal: [its.usiu.ac.ke](https://its.usiu.ac.ke)                     
- 📍 Location: USIU Road, Off Thika Road (Exit 7), Nairobi, Kenya
""")
