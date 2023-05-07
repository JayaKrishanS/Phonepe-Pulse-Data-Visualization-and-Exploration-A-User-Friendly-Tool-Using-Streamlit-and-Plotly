from sqlalchemy import create_engine
import pandas as pd
from PIL import Image
import streamlit as st
import psycopg2
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title='PhonePay India Dashboards', layout='wide')
st.title('&emsp;&emsp;**Phonepe-Pulse Data Visualization**')


st.sidebar.header('**Dashboard**')
add_selectbox = st.sidebar.selectbox(
    "**Select an option**",
    ("user","transaction",)
)

col1,col2=st.sidebar.columns(2)

if add_selectbox=='user' or 'transaction':
    with col1:
        year=st.selectbox('**Select an option**',(2018,2019,2020,2021,2022))
        if year==2018:
            quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
        elif year==2019:
            quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
        elif year==2020:
            quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
        elif year==2021:
            quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
        elif year==2022:
            quarter=st.selectbox('Select an option',('Q1(Jan-March)','Q2(Apr-June)','Q3(July-Sep)','Q4(Oct-Dec)'))
types=st.sidebar.selectbox("**Select an option**",('Aggregation','Top_list'))


connection = psycopg2.connect(database="Phonepe-Pulse", user="postgres", password="Jaya@9698", host="localhost", port="5432")

query_AT = "SELECT * FROM aggregated_transaction"
df_agg_trans = pd.read_sql_query(query_AT, connection)

query_AU = "SELECT * FROM aggregated_user"
df_agg_users = pd.read_sql_query(query_AU, connection)

query_MT = "SELECT * FROM map_transactions"
df_map_trans = pd.read_sql_query(query_MT, connection)

query_MU = "SELECT * FROM map_users"
df_map_users = pd.read_sql_query(query_MU, connection)

query_TT = "SELECT * FROM top_transactions"
df_top_trans = pd.read_sql_query(query_TT, connection)

query_TU = "SELECT * FROM top_users"
df_top_users = pd.read_sql_query(query_TU, connection)


if add_selectbox == 'user':
        if year == 2018:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2018) & (df_agg_users['quarter'] == 1)]
                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000),title='Bar chart representation')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)

                    fig3 = px.pie(filtered_df,names='device_brands',values='counts',title='Pie chart representation')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state',title='Sunburst chart representation')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)


                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 1)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 1)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2018) & (df_agg_users['quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 2)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 2)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)
            
            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2018) & (df_agg_users['quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)

                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                    st.write('Output for user, year=2018, quarter=Q2, and type=Aggregation')
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 3)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 3)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2018) & (df_agg_users['quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 4)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 4)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

        if year == 2019:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2019) & (df_agg_users['quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2019) & (df_top_users['quarter'] == 1)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 1)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2019) & (df_agg_users['quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2019) & (df_top_users['quarter'] == 2)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 2)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2019) & (df_agg_users['quarter'] ==3)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2019) & (df_top_users['quarter'] == 3)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 3)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2019) & (df_agg_users['quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2019) & (df_top_users['quarter'] == 4)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 4)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)


        if year == 2020:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2020) & (df_agg_users['quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2020) & (df_top_users['quarter'] == 1)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 1)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2020) & (df_agg_users['quarter'] == 2)]

                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)

                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2020) & (df_top_users['quarter'] == 2)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 2)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2020) & (df_agg_users['quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2020) & (df_top_users['quarter'] == 3)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 3)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2020) & (df_agg_users['quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2020) & (df_top_users['quarter'] == 4)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 4)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

        if year == 2021:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2021) & (df_agg_users['quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2021) & (df_top_users['quarter'] == 1)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 1)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2021) & (df_agg_users['quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2021) & (df_top_users['quarter'] == 2)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 2)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2021) & (df_agg_users['quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2021) & (df_top_users['quarter'] == 3)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 3)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2021) & (df_agg_users['quarter'] == 4)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2021) & (df_top_users['quarter'] == 4)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 4)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

        if year == 2022:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2022) & (df_agg_users['quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2022) & (df_top_users['quarter'] == 1)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 1)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2022) & (df_agg_users['quarter'] == 2)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2022) & (df_top_users['quarter'] == 2)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 2)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2022) & (df_agg_users['quarter'] == 3)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2022) & (df_top_users['quarter'] == 3)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 3)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df = df_agg_users[(df_agg_users['year'] == 2022) & (df_agg_users['quarter'] == 1)]


                    fig1=px.bar(filtered_df,x='device_brands',y='counts',hover_name='state',color='state',range_y=(0,13000000))
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='device_brands',values='counts')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','device_brands'],values='counts',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    col,col1=st.columns(2)
                    with col:
                        tts=st.button('Top 10 state')
                        if tts:
                            filtered_df = df_top_users[(df_top_users['year'] == 2022) & (df_top_users['quarter'] == 4)]
                            state_counts=filtered_df.groupby('state').agg({'registered_user':'sum'})
                            sorted_counts=state_counts.sort_values('registered_user',ascending=False)
                            top_ten_states=sorted_counts.head(10)
                            st.dataframe(top_ten_states)

                            fig = px.bar(top_ten_states, x=top_ten_states.index, y='registered_user', labels={'x':'state', 'registered_user':'registered users'})
                            st.plotly_chart(fig)

                            fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)
                    with col1:
                        ttp=st.button('Top 10 pincodes')
                        if ttp:
                            filtered_df = df_top_users[(df_top_users['year'] == 2018) & (df_top_users['quarter'] == 4)]
                            pin_counts=filtered_df.groupby('pincode').agg({'registered_user':'sum'})
                            sort_counts=pin_counts.sort_values('registered_user',ascending=False)
                            top_ten_pin=sort_counts.head(10)
                            st.dataframe(top_ten_pin)


                            fig1 = px.pie(top_ten_pin, names=top_ten_pin.index, values='registered_user')
                            fig1.update_traces(textposition='outside')
                            st.plotly_chart(fig1)

                            fig2=go.Figure(go.Pie(labels=top_ten_pin.index,values=top_ten_pin['registered_user'],hole=0.5))
                            st.plotly_chart(fig2)

if add_selectbox == 'transaction':
        if year == 2018:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==1)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==1)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)



            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==2)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==2)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==3)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==3)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==4)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2018)&(df_agg_trans['quarter']==4)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

        if year == 2019:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==1)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==1)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==2)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==2)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==3)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==3)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==4)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2019)&(df_agg_trans['quarter']==4)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)


        if year == 2020:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==1)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==1)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==2)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==2)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==3)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==3)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==4)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2020)&(df_agg_trans['quarter']==4)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

        if year == 2021:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==1)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==1)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==2)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==2)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==3)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==3)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==4)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2021)&(df_agg_trans['quarter']==4)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

        if year == 2022:
            if quarter == 'Q1(Jan-March)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==1)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==1)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q2(Apr-June)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==2)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==2)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q3(July-Sep)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==3)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==3)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)

            elif quarter == 'Q4(Oct-Dec)':
                if types == 'Aggregation':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==4)]

                    fig1=px.bar(filtered_df,x='transaction_type',y='transaction_count',hover_name='transaction_amount',color='state',range_y=(0,10000000),animation_frame='state')
                    fig1_f = fig1.update_layout(width=800,height=650,)
                    st.plotly_chart(fig1_f)


                    fig3 = px.pie(filtered_df,names='transaction_type',values='transaction_count')
                    fig_f = fig3.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)

                    fig4=px.sunburst(filtered_df,path=['state','transaction_type'],values='transaction_count',color='state')
                    fig_f = fig4.update_layout(width=800,height=650,)
                    st.plotly_chart(fig_f)
                elif types == 'Top_list':
                    filtered_df=df_agg_trans[(df_agg_trans['year']==2022)&(df_agg_trans['quarter']==4)]     
                    state_counts=filtered_df.groupby('state').agg({'transaction_count':'sum','transaction_amount':'sum'})
                    sorted_counts=state_counts.sort_values('transaction_count',ascending=False)
                    top_ten_states=sorted_counts.head(10)
                    st.dataframe(top_ten_states)
                    fig = px.bar(top_ten_states, x=top_ten_states.index, y='transaction_count', labels={'x':'state', 'y':'registered users'})
                    st.plotly_chart(fig)

                    fig1 = px.pie(top_ten_states, names=top_ten_states.index, values='transaction_amount')
                    fig1.update_traces(textposition='outside')
                    st.plotly_chart(fig1)