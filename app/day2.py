import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

st.title(":material/smart_toy: Hello, Cortex!")

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create() 


st.write(session.connection.warehouse)
st.write(session.session_id)
#session.use_warehouse("COMPUTE_WH")
st.write(session.sql("""
    SELECT CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA()
""").collect())
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
