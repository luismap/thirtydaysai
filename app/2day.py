import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

st.title(":material/smart_toy: Hello, Cortex!")

"""main functions"""
# Connect to Snowflake
#lets cache and reuse same session
@st.cache_resource
def get_session():
    try:
        # Works in Streamlit in Snowflake
        from snowflake.snowpark.context import get_active_session
        session = get_active_session()
    except:
        # Works locally and on Streamlit Community Cloud
        from snowflake.snowpark import Session
        session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create() 
    return session

#cache the query in streamlit side, for savings
@st.cache_data(ttl=3600)  # ttl=3600 means the cache expires after 1 hour
def run_query(query):
    # .collect() pulls the data into the app's memory as a list of Rows
    return session.sql(query).collect()

session = get_session()

"""sider section"""
# 1. Setup the Sidebar UI
with st.sidebar:
    st.header("App Controls")
    if st.button("🔄 Refresh Data"):
        # This clears all functions decorated with @st.cache_data
        st.cache_data.clear()
        st.cache_resource.clear()
        st.toast("Cache cleared! Re-fetching from Snowflake...")
        st.rerun()


st.write(session.connection.warehouse)
st.write(session.session_id)
#session.use_warehouse("COMPUTE_WH")
st.write(run_query("SELECT CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA()"))

# Model and prompt
model = "claude-3-5-sonnet"
prompt = st.text_input("Enter your prompt:")

# Run LLM inference
if st.button("Generate Response"):
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt).alias("response")
    )
    
    # Get and display response
    response_raw = df.collect()[0][0]
    response = json.loads(response_raw)
    st.write(response)

# Footer
st.divider()
st.caption("Day 2: Hello, Cortex! | 30 Days of AI")
