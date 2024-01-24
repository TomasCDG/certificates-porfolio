import streamlit as st
from about import about_str, intro, core

st.set_page_config(
    page_title="Tomi Di Gennaro",
    page_icon="🤓",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"About": about_str},
)


# Intro
st.write(intro)
st.image(
    "profile_pic/profile.jpg",
    width=250,
)

# about me
st.header("*About me*")
st.write(core)
st.write ("**The rest of the pages are in the sidebar on the left, if you can't find it, try it on another device or change resolution 🙏**")

st.divider()

# instruction


st.write("### *A few words about me*")
st.subheader("Environmental Engineering career")
st.write("In 2019 I graduated in Environmental Engineering In National University of General San Martín, Argentina.",
         "\n\nDuring that part of my professional career, I worked as a sort of trainee **data analyst** (there wasn't that name for that job yet) for the *National Ministry of Energy and Mining* "
         "\n\n Later, I worked as an environmental inspector for the Water Authority of the Province of Buenos Aires, while still working as a teacher assistant at my univeristy"
         )

st.subheader("Data Science career")

st.write("##### Le Wagoon - Bootcamp",
        "\n\n In 2020, having studied Python, SQL and took the data science bootcamp at **Le Wagon**.",
         "\n\n In 2021 I started working as a teacher assistant, becoming eventually a teacher, and ultimately becoming lead teacher and manager of the courses.",
        "\n\n During that time, I also partook in some freelance data analysis projects for ONGs like *'Un Techo para Mi país' ('A roof for my country')*",
)
st.write("##### Changomás - Retail",
        "\n\n In 2022, I joined Changomás (formerly called Walmart) as a data scientist. My main responsibilities included",
        "My main responsibilities included the development of ETL pipelines that integrate information from diverse sources (internal and external databases, dashboards, third party apps and API services) into *PowerBI* and *Microstrategy* dashboards, as well as scheduled emails to executives with attached automated reports, or even other target databases for storage.",
        "\n\n Other responsibilities included developing live performance analysis during ongoing special events (eg. Black Friday)",
)

st.write("##### Traditum - Healthtech",
        "\n\n In 2023 I Joined Traditum, a healthtech company, as a data Engineer. My responsibilities included again the development of ETL pipelines, in order to manage customer and practitioners' information in the systems",
        "\n\n I also had the opportunity to develop NLP models to automate and optimize the information processing in these pipelines"
        
        "\n\n During that year, I also had the chance to work on freelance data science profits using Large models like MediaPipe libraries for video processing and tracking people's interactions with products in supermarkets' CCTV cameras"
        "\n\n Another project included the use of Huggingface models for Document Named Entity Recognition in app built for carbon footprint calculations"
)        
st.write ( "##### Globant",
        "\n\n In December, 2023, I joined Globant as a data scientist, integrating LLMs with technologies like LangChanin."
        
         )
