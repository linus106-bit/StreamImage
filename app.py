import streamlit as st
import pandas as pd
import json
st.title("Stream Image")

def update(edf,page):
    # edf.to_csv(csvfn, index=False)
    list_from_df = edf.values.tolist()
    print(list_from_df)
    json_data[page]['conversations'] = list_from_df
    # 이걸 다시 json으로 dump?
    with open('dataset_backup.json','w') as f:
        json.dump(json_data,f,indent=2,ensure_ascii=False)


if __name__=='__main__':
    if 'page' not in st.session_state:
        st.session_state.page = 0

    # Create next and previous buttons with session state management
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Previous'):
            if st.session_state.page > 0:
                st.session_state.page -= 1

    with col2:
        if st.button('Next'):
            if (st.session_state.page + 1) < 10:
                st.session_state.page += 1

    page = st.session_state.page
    st.write(page)
    with open('dataset.json','r') as f:
        json_data = json.load(f)
    df = pd.DataFrame(json_data[page]['conversations'],columns=['question','answer'])
    # # Header 추가
    edited_df = st.data_editor(df,num_rows="dynamic")
    st.button('Save', on_click=update, args=(edited_df, page))
