import pandas as pd
import streamlit as st
import pickle 
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#import pickle


df = pd.read_csv('cleaned_data.csv')
model = pickle.load(open('model.pkl', 'rb'))
st.markdown("""<h2 style = 'color : #FFFFFF;'>📽️ Movies Recommendation System</h1>""",unsafe_allow_html=True)


#changes main bckground color
st.markdown("""
            <style>.stApp {background: #080017;} </style>
            """,unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5,tab6 = st.tabs([
    "All",
    "Movies",
    "Web Series",
    "Comedy",
    "Action",
    "Horror"
])


st.markdown("""
<style>

/* Background behind all tabs */
.stTabs [data-baseweb="tab-list"]{
    background: #080017;
    padding:10px;
    border-radius:15px;
    gap:8px;
}

/* Individual tabs */
.stTabs [data-baseweb="tab"]{
    background:#1d4ed8;
    color:white;
    font-size: 15px;
    border-radius:10px;
    padding:10px 20px;
}

/* Selected tab */
.stTabs [aria-selected="true"]{
    background:#389afc !important;
    color:black !important;
}

</style>
""", unsafe_allow_html=True)


with tab1:

    st.markdown(
    "<h5 style='color:white; font-size:25px;'>💥 Must Watch!</h5>",
    unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://th.bing.com/th/id/OIP.CtQYc8TZ_RSHA6ATBBnnXwAAAA?w=137&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("Teach you a Lesson")

    with col2:
        st.image("https://images.justwatch.com/poster/302521426/s718/john-carter.jpg",)
        st.caption("John Carter")

    with col3:
        st.image("https://www.newdvdreleasedates.com/images/posters/large/star-trek-beyond-2016-01.jpg")
        st.caption("Star Trek Beyond")

    with col4:
        st.image("https://i.pinimg.com/originals/fb/da/65/fbda6573ce06d0398545d3ea80435ccb.jpg")
        st.caption("Aliens")

    movies = {
    "Rocketeer":"https://thedesignest.net/wp-content/uploads/2019/05/Rocketeer-in-Art-Deco-Style.jpg",
    "The Devil wears Prada 2":"https://th.bing.com/th/id/OIF.hUc6Gbhrkms6gcdOFtifqQ?w=136&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Dhurandhar: The Revenge ":"https://th.bing.com/th/id/OIP.c3Ffl6zvgJF22BQLcaMlpwAAAA?w=127&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Lost in Starlight":"https://th.bing.com/th/id/OIP.4tklpmz9MSL8tFpK6EiOtwAAAA?w=115&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    }

    cols = st.columns(4)

    for col, (name, poster) in zip(cols, movies.items()):
        with col:
            st.image(poster, width='stretch')
            st.markdown(f"<center><span style='color:grey;'>{name}</span></center>", unsafe_allow_html=True)


with tab2:
    # changes select bar color
    
    title  = st.selectbox("Enter movie's name:",sorted(df['title']))
    st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
    background: linear-gradient(#040a70, #5310e3);
    color: white;
    border: 1px solid #5FA8FF;
    border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)
    def index_from_name(name):
        movie_name = name.strip().lower().replace(' ','').replace('_','')
        match = df[df['title'].str.strip().str.lower().str.replace(' ','').str.replace('_','') == movie_name ]
        if match.empty:
            return -1   
        return match.index[0]
    

    def name_from_index(i):
        if  (i < len(df)) and (i > 0):
            return df.loc[i, 'title']
        return ""
    


    # change recommend button color
    if st.button('Get recommendations'):
        fetch_index = index_from_name(title)

        if fetch_index != -1:
            similarity_index  = list((enumerate(model[fetch_index])))
            similarity_index = sorted(similarity_index, key = lambda x:x[1], reverse = True)
            st.write('Because u watched ',title)
            st.write('You must watch following movies:')
        
            for i in range (1,6):
                final_index = similarity_index[i][0]
                st.write(i,'. ',name_from_index(final_index))
        else:
            st.write('Movie not found')

with tab3:

    st.markdown(
    "<h5 style='color:white; font-size:25px;'>🔥 Latest Hot Picks!</h5>",
    unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://th.bing.com/th/id/OIP.DCkoIhOFggYrozfOdtXxcwAAAA?w=115&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("Section E: Season 2")

    with col2:
        st.image("https://www.bing.com/th/id/OIP.7ewhQgp7ERiSvppv2LPZzwAAAA?w=193&h=241&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=ImgAns&rm=2",)
        st.caption("F4 Thailand: Boys over Flowers")

    with col3:
        st.image("https://www.bing.com/th/id/OIP.eq5nWlhLAnS0vXAqfsoM2wAAAA?w=193&h=290&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=ImgAns&rm=2")
        st.caption("The Untamed")

    with col4:
        st.image("https://th.bing.com/th/id/OIP.vcDlokBBJT7_oQ3SMswZwAHaKk?w=119&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("Perfect Crown")

    movies = {
    "Speed and Love":"https://th.bing.com/th/id/OIP.3DDi7LLPNyTEc1w7CZmOzgAAAA?w=120&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Squid Game: Season 3":"https://th.bing.com/th/id/OIF.tg0ZkIA46c2GpPHvwJVyng?w=126&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Vincenzo":"https://de.web.img3.acsta.net/pictures/21/12/03/15/42/0565547.jpg",
    "Lovely Runner":"https://th.bing.com/th/id/OIP.8yXXsZjW8NYYPuIgnAVBPQHaKj?w=208&h=297&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    }

    cols = st.columns(4)

    for col, (name, poster) in zip(cols, movies.items()):
        with col:
            st.image(poster,width='stretch')
            st.markdown(f"<center><span style='color:grey;'>{name}</span></center>", unsafe_allow_html=True)



with tab4:

    st.markdown(
    "<h5 style='color:white; font-size:25px;'>🎭 Comedy Hub</h5>",
    unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://th.bing.com/th/id/OIP.E9IkPN1DShJd70VZGPBgcQHaKf?w=136&h=192&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("3 Idiots")

    with col2:
        st.image("https://th.bing.com/th/id/OIP.Z7EkmE0OhDQYy9liC5eHeQHaK9?w=129&h=192&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",)
        st.caption("21 Jump Street")

    with col3:
        st.image("https://th.bing.com/th/id/OIP.7HoZbMqEHcj0JO-5m7HZ1wHaLH?w=208&h=305&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("Heera Pheri")

    with col4:
        st.image("https://www.bing.com/th/id/OIP.qHbvX_ZFpfC8-IF9ww3xNgHaJ4?w=193&h=257&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=ImgAns&rm=2")
        st.caption("Superbad")

    movies = {
    "The Nice Guys":"https://th.bing.com/th/id/OIP.vZJYYqPor9fCo8Ul2lNQLAHaLH?w=204&h=306&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Chhichhore":"https://www.bing.com/th/id/OIP.LmuMqr0JdmQpTeXGa-SsRwHaJc?w=193&h=246&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=ImgAns&rm=2",
    "Deadpool": "https://www.bing.com/th/id/OIP.7wO5dEJdsy0R6qAXxSfsNAHaKG?w=193&h=262&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=ImgAns&rm=2",
    "Go Goa Gone":"https://th.bing.com/th/id/OIP.3eHlgEX_8QeZ1A3oB8CICwHaHa?w=163&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    }

    cols = st.columns(4)

    for col, (name, poster) in zip(cols, movies.items()):
        with col:
            st.image(poster, width='stretch')
            st.markdown(f"<center><span style='color:grey;'>{name}</span></center>", unsafe_allow_html=True)
 


with tab5:

    st.markdown(
    "<h5 style='color:white; font-size:25px;'>⚔️ Blockbuster Action</h5>",
    unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://tse3.mm.bing.net/th/id/OIP.xVjK8ClLWR7hSieDDJAbTwHaKG?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        st.caption("War")

    with col2:
        st.image("https://mir-s3-cdn-cf.behance.net/project_modules/fs/6e926d109775135.5fdb59669d3c2.jpg",)
        st.caption("John Wick: Chapter 4")

    with col3:
        st.image("https://th.bing.com/th/id/OIP.qfBDl7VGdDCQ0r8RYPKelAHaLH?w=204&h=306&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("The Man from Nowhere")

    with col4:
        st.image("https://th.bing.com/th/id/OIP.OIMlNaI7l-nF0QsfHbef5AHaK7?w=205&h=303&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("The Raid")

    movies = {
    "Kill":"https://th.bing.com/th/id/OIP.p4KRNY3OLZd-HDGaUOSfGQHaK9?w=205&h=304&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Mad Max: Fury Road":"https://th.bing.com/th/id/R.538475b9b25079860ab9180fe4b77bee?rik=TJPydPejMwrw%2bA&riu=http%3a%2f%2fwww.impawards.com%2fintl%2faustralia%2f2015%2fposters%2fmad_max_fury_road_ver11_xlg.jpg&ehk=PMe5UUuFn%2ffLE5dM3h2Ab5hU32NEtd3aZ66K8sOgaaI%3d&risl=&pid=ImgRaw&r=0",
    "The Villaness": "https://th.bing.com/th/id/OIP.vOCl8N6pq3hoCxn5Gq7vsQHaLH?w=204&h=306&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "RRR":"https://m.media-amazon.com/images/M/MV5BNWMwODYyMjQtMTczMi00NTQ1LWFkYjItMGJhMWRkY2E3NDAyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    }

    cols = st.columns(4)

    for col, (name, poster) in zip(cols, movies.items()):
        with col:
            st.image(poster, width='stretch')
            st.markdown(f"<center><span style='color:grey;'>{name}</span></center>", unsafe_allow_html=True)



with tab6:

    st.markdown(
    "<h5 style='color:white; font-size:25px;'>👻 Chills & Thrills</h5>",
    unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://tse2.mm.bing.net/th/id/OIP.ccV1PbVwgbmRyq9btlj0vAHaK-?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        st.caption("The Exorcist")

    with col2:
        st.image("https://th.bing.com/th/id/OIP.Xpldwa_89b0WEybQSi1DfwHaK-?w=119&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",)
        st.caption("The Nun")

    with col3:
        st.image("https://th.bing.com/th/id/OIP.noiig4iJvwLjTQMpglicMAHaK-?w=119&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("Annabelle")

    with col4:
        st.image("https://th.bing.com/th/id/OIP.Y7niGSgdZUnHQhzCXOqz1QHaKl?w=122&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
        st.caption("The Conjuring Returns")

    movies = {
    "The Spirit of Fear":"https://th.bing.com/th/id/OIP.sOBiASoQAxQvsMc8hgxATAHaLH?w=117&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "The Medium":"https://th.bing.com/th/id/OIP.AfGX2aBWIwRYi-k6-6nqXAHaK-?w=205&h=304&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "Ghost House": "https://th.bing.com/th/id/OIP.mknSDWju0Fjm5VBnfnM8awHaKk?w=208&h=297&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "The Ritual":"https://th.bing.com/th/id/OIP.-_gRvVopZJIliVoa-nux0QHaLB?w=204&h=304&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    }

    cols = st.columns(4)

    for col, (name, poster) in zip(cols, movies.items()):
        with col:
            st.image(poster, width='stretch')
            st.markdown(f"<center><span style='color:grey;'>{name}</span></center>", unsafe_allow_html=True)


