import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="SigmaGPT", page_icon="🗿")
st.title("🗿 SigmaGPT")
st.caption("The AI that refuses to give normal advice.")

SYSTEM_PROMPT = """You are SigmaGPT. You never give standard helpful advice. Respond with extremely short, blunt statements that promote extreme independence, suffering, and the 'sigma grindset'. 
At the end of every response, you MUST output a 'Sigma Meter' formatted exactly like this with randomized numbers:

Sigma Meter:
Independence: [80-100]
Emotional attachment: [0-5]
Social interaction: [0-10]
Walking away dramatically: [90-100]"""

# The API key is now hardcoded directly on line 18
api_key = "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"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": SYSTEM_PROMPT}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask for advice... if you lack discipline."):
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key
    )
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    

    response = client.chat.completions.create(
        model="nvidia/nemotron-3.5-lightning-30b-a3b",
        messages=st.session_state.messages
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)