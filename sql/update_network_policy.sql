use role accountadmin;

create or replace network policy my_streamlit
allowed_ip_list = ('your ip');

ALTER ACCOUNT SET NETWORK_POLICY = my_streamlit;
