import psycopg2
import time
import requests
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

hostname = 'localhost'
database = 'Netflix'
port_id = 5432
username = 'postgres'
pwd = 'postgrey'

conn=None
cur=None

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

conn=psycopg2.connect(
    host=hostname,
    port=port_id,
    dbname=database,
    user=username,
    password=pwd
)

cur = conn.cursor()

#PAGE DEETS
st.set_page_config(page_icon=":tada",layout="wide")

def new_password(hashed_passwords):
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("wb") as file:
        pickle.dump(hashed_passwords, file)

    file_path=Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

names_list = ["Ernest Barnes","Andrea Baker","Rebecca Parker","Laura Murray","Linda Hines","Jasmine Fletcher","Dylan Rangel","William Velez","Steven Murphy","Michael Moore","Priscilla Collins","Laurie Smith","Casey Thomas","Rachel Friedman","Edward Torres","Samuel Zavala","Dr. Victor Martin","Sara Lee","Curtis Rodriguez","Stephanie Schmidt","John Matthews"]
usernames = ["5008804","5008805","5008806","5008808","5008809","5008810","5008811","5008812","5008813","5008814","5008815","5112956","6153651","5008819","5008820","5008821","5008822","5008823","5008824","5008825","5008826"]
passwords = ["652-885-2745", "364-656-8427","713-226-5883","190-271-6743","420-332-5209","286-669-4333","341-726-5787","316-648-6176","833-887-7898","804-383-4080","211-071-2173","435-075-8409","790-746-7471","649-384-5387","331-430-8824","573-306-9938","466-424-2102","896-642-1049","952-496-4398","382-465-6552","784-675-4921"]

hashed_passwords = stauth.Hasher(passwords).generate()
new_password(hashed_passwords)

authenticator = stauth.Authenticate(names_list, usernames, hashed_passwords,
                                    "sales_dashboard", "abcdef", cookie_expiry_days=30)

names_list, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter username and password")

if authentication_status:
    #ANIMATION
    with st.container():
        lottie_url_download="https://assets8.lottiefiles.com/private_files/lf30_F6EtR7.json"
        lottie_download=load_lottieurl(lottie_url_download)

        st_lottie(
            lottie_download,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",
            height=None,
            width=None,
            key=None,
            )
                
    #HEADER
    with st.container():
        st.subheader("Watch Movies, TV Shows and More :cinema:")
        st.title("Netflix")
        st.write("One-stop-shop for all things related to Movies and TV Shows")
        st.write("EXPLORE, DISCOVER AND ENJOY :camera:")
        st.write("[Netflix.com >](https://www.netflix.com/in/)")
        st.write("---") #DIVIDER

    #INCLUDING PACKAGES FOR LATEST RELEASE(MOVIES)
    with st.container():
        st.header("NEW MOVIE RELEASES")
        cur.execute("select movname from movies where movryear>2021")
        arr=cur.fetchall()
        for i in arr:
            for j in i:
                st.text(j)
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form1=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\thunivu.jpg")
            st.image(img_contact_form1)
            with text_column:
                st.subheader("THUNIVU (Tamil)")
                st.markdown("[Watch Trailer...](https://youtu.be/jnBZboK17_A)")
                cur.execute("select description from movies where movname='Thunivu'")
                arr_thunivu=cur.fetchall()
                for i in arr_thunivu:
                    for j in i:
                        st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form2=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\kaatteri.jpg")
            st.image(img_contact_form2)
            with text_column:
                st.subheader("KATTERI (Tamil)")
                st.markdown("[Watch Trailer...](https://youtu.be/4-Ss4wruL6k)")
                cur.execute("select description from movies where movname='Kaatteri'")
                arr_katt=cur.fetchall()
                for i in arr_katt:
                    for j in i:
                        st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form3=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\raangi.jpg")
            st.image(img_contact_form3)
        with text_column:
            st.subheader("RAANGI (Tamil)")
            st.markdown("[Watch Trailer...](https://youtu.be/77jiph_JMNI)")
            cur.execute("select description from movies where movname='Raangi'")
            arr_raa=cur.fetchall()
            for i in arr_raa:
                for j in i:
                    st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form4=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\CBI 5.jpg")
            st.image(img_contact_form4)
            with text_column:
                st.subheader("CBI 5:THE BRAIN (Malayalam)")
                st.markdown("[Watch Trailer...](https://youtu.be/PKbL-427wms)")
                cur.execute("select description from movies where movname='CBI 5: The Brain'")
                arr_cbi=cur.fetchall()
                for i in arr_cbi:
                    for j in i:
                        st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form5=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\drifting home.jpg")
            st.image(img_contact_form5)
        with text_column:
            st.subheader("DRIFTING HOME (English)")
            st.markdown("[Watch Trailer...](https://youtu.be/BSE2KGU5png)")
            cur.execute("select description from movies where movname='Drifting Home'")
            arr_drif=cur.fetchall()
            for i in arr_drif:
                for j in i:
                    st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form6=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\the adam project.jpg")
            st.image(img_contact_form6)
        with text_column:
            st.subheader("THE ADAM PROJECT (English)")
            st.markdown("[Watch Trailer...](https://youtu.be/IE8HIsIrq4o)")
            cur.execute("select description from movies where movname='The Adam Project'")
            arr_tap=cur.fetchall()
            for i in arr_tap:
                for j in i:
                    st.text(j)

    with st.container():
        st.header("NEW TV SHOW RELEASES")
        cur.execute("select tvname from tvshows where tvryear>2021")
        arr_tv=cur.fetchall()
        for i in arr_tv:
            for j in i:
                st.text(j)
        #HEARTSTOPPER
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form10=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\heartstopper.png")
            st.image(img_contact_form10)
            with text_column:
                st.subheader("HEARTSTOPPER (English)")
                st.markdown("[Watch Trailer...](https://youtu.be/FrK4xPy4ahg)")
                cur.execute("select description from tvshows where tvname='Heartstopper'")
                arr_h=cur.fetchall()
                for i in arr_h:
                    for j in i:
                        st.text(j)
    #GDTCOC
    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form11=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\gdtcoc.jpg")
            st.image(img_contact_form11)
        with text_column:
            st.subheader("GUILLERMO DEL TORO'S CABINET OF CURIOSTITIES (English)")
            st.markdown("[Watch Trailer...](https://youtu.be/E3E1URhCR60)")
            cur.execute("select description from tvshows where tvname='Guillermo del Toros Cabinet of Curiosities'")
            arr_gdt=cur.fetchall()
            for i in arr_gdt:
                for j in i:
                    st.text(j)

    #WEDNESDAY
    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form11=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\wednesday.jpg")
            st.image(img_contact_form11)
        with text_column:
            st.subheader("WEDNESDAY (English)")
            st.markdown("[Watch Trailer...](https://youtu.be/Di310WS8zLk)")
            cur.execute("select description from tvshows where tvname='Wednesday'")
            arr_wed=cur.fetchall()
            for i in arr_wed:
                for j in i:
                    st.text(j)

    #HINDI MOVIES
    with st.container():
        st.header("HINDI")
        cur.execute("select movname from movies where languages='Hindi'")
        arr=cur.fetchall()
        for i in arr:
            for j in i:
                st.text(j)
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form7=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\gangs of wasseypur.jpg")
            st.image(img_contact_form7)
        with text_column:
            st.subheader("GANGS OF WASSEYPUR")
            st.write("Actors:")
            cur.execute("select actors from movies where movname='Gangs of wasseypur'")
            arr1=cur.fetchall()
            for i in arr1:
                for j in i:
                    st.text(j)
            st.text("Duration:")
            cur.execute("select duration from movies where movname='Gangs of wasseypur'")
            arr2=cur.fetchall()
            for i in arr2:
                for j in i:
                    st.text(j)
            st.text("IMDB Rating:")
            cur.execute("select imdb from movies where movname='Gangs of wasseypur'")
            arr3=cur.fetchall()
            for i in arr3:
                for j in i:
                    st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form8=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\jab we met.jpg")
            st.image(img_contact_form8)
            with text_column:
                st.subheader("JAB WE MET")
                st.text("Actors:")
                cur.execute("select actors from movies where movname='Jab we met'")
                arr_jwm=cur.fetchall()
                for i in arr_jwm:
                    for j in i:
                        st.text(j)
                st.text("Duration:")
                cur.execute("select duration from movies where movname='Jab we met'")
                arr_jwmd=cur.fetchall()
                for i in arr_jwmd:
                    for j in i:
                        st.text(j)
                st.text("IMDB Rating:")
                cur.execute("select imdb from movies where movname='Jab we met'")
                arr_jwmi=cur.fetchall()
                for i in arr_jwmi:
                    for j in i:
                        st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form8=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\3 idiots.jpg")
            st.image(img_contact_form8)
        with text_column:
            st.subheader("3 IDIOTS")
            st.text("Actors:")
            cur.execute("select actors from movies where movname='3 idiots'")
            arr_3=cur.fetchall()
            for i in arr_3:
                for j in i:
                    st.text(j)            
            st.text("Duration:")
            cur.execute("select duration from movies where movname='3 idiots'")
            arr_3d=cur.fetchall()
            for i in arr_3d:
                for j in i:
                    st.text(j)
            st.text("IMDB Rating:")
            cur.execute("select imdb from movies where movname='3 idiots'")
            arr_3i=cur.fetchall()
            for i in arr_3i:
                for j in i:
                    st.text(j)

    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form8=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\stree.jpg")
            st.image(img_contact_form8)
            with text_column:
                st.subheader("STREE")
                st.text("Actors:")
                cur.execute("select actors from movies where movname='Stree'")
                arr_stree=cur.fetchall()
                for i in arr_stree:
                    for j in i:
                        st.text(j)
                st.text("Duration:")
                cur.execute("select duration from movies where movname='Stree'")
                arr_streed=cur.fetchall()
                for i in arr_streed:
                    for j in i:
                        st.text(j)
                st.text("IMDB Rating:")
                cur.execute("select imdb from movies where movname='Stree'")
                arr_streei=cur.fetchall()
                for i in arr_streei:
                    for j in i:
                        st.text(j)
    with st.container():
        image_column, text_column=st.columns((1,2))
        with image_column:
            img_contact_form8=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\andhadhun.jpg")
            st.image(img_contact_form8)
        with text_column:
            st.subheader("ANDHADHUN")
            st.text("Actors:")
            cur.execute("select actors from movies where movname='Andhadhun'")
            arr_a=cur.fetchall()
            for i in arr_a:
                for j in i:
                    st.text(j)
            st.text("Duration:")
            cur.execute("select duration from movies where movname='Andhadhun'")
            arr_ad=cur.fetchall()
            for i in arr_ad:
                for j in i:
                    st.text(j)
            st.text("IMDB Rating:")
            cur.execute("select imdb from movies where movname='Andhadhun'")
            arr_ai=cur.fetchall()
            for i in arr_ai:
                for j in i:
                    st.text(j)

    with st.container():
        st.header(":film_frames: Subscription Plans Available:")
        image_column, text_column=st.columns((1,1))
        with image_column:
            img_contact_form12=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\images\\plans.png")
            st.image(img_contact_form12)
        with text_column:
            st.text(" ")

    #SIDEBAR DEETS
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {names_list}")

    #USER INPUT FOR MOVIES
    genre_input="'Genre'"
    languages_input="'Language'"

    #MOVIES
    st.header("Search for Movies:")
    genre=["Select genre","'Action'","'Romance'","'Comedy'","'Thriller'","'Sci-fi'"]
    languages=["Select language","'English'","'Hindi'","'Tamil'","'Malayalam'"]
    genre_input="'Genre'"
    languages_input="'Language'"
    genre_input=st.selectbox('Genre:',genre, index=1)
    languages_input=st.selectbox('Language',languages, index=1)
    mov=[]
    str_mn="select movname from movies where genres="+genre_input+"and languages="+languages_input
    cur.execute(str_mn)
    mov=cur.fetchall()
    st.text("MOVIE NAME:")
    for i in mov:
        for j in i:
            st.text(j)
    #GETTING ACTORS
    str_a="select actors from movies where genres="+genre_input+"and languages="+languages_input
    cur.execute(str_a)
    mov1=cur.fetchall()
    st.text("ACTORS:")
    for i in mov1:
        for j in i:
            st.text(j)
    #GETTING DIRECTORS
    str_d="select director from movies where genres="+genre_input+"and languages="+languages_input
    cur.execute(str_d)
    mov2=cur.fetchall()
    st.text("DIRECTORS:")
    for i in mov2:
        for j in i:
            st.text(j)
    #GETTING DURATION OF THE MOVIE
    str_dd="select duration from movies where genres="+genre_input+"and languages="+languages_input
    cur.execute(str_dd)
    mov5=cur.fetchall()
    st.text("DURATION:")
    for i in mov5:
        for j in i:
            st.text(j)
    #GETTING AGE RATING
    str_aa="select agerating from movies where genres="+genre_input+"and languages="+languages_input
    cur.execute(str_aa)
    mov3=cur.fetchall()
    st.text("AGE RATING:")
    for i in mov3:
        for j in i:
            st.text(j)
    #GETTING IMDB RATING
    str_i="select imdb from movies where genres="+genre_input+"and languages="+languages_input
    cur.execute(str_i)
    mov4=cur.fetchall()
    st.text("IMDB RATING:")
    for i in mov4:
        for j in i:
            st.text(j)

    #TV SHOWS
    st.header("Search for TV Shows:")
    tvgenre=["Select genre","'Action'","'Romance'","'Comedy'","'Thriller'","'Sci-fi'","'Anime'"]
    tvlanguages=["Select language","'English'","'Hindi'"]
    #tvgenre="'Genre'"
    #tvlanguages="'Languages'"
    tvgenre=st.selectbox('Genre:',tvgenre, index=1)
    tvlanguages=st.selectbox('Language',tvlanguages, index=1)
    #TV SHOW NAME
    tv=[]
    str_tvn="select tvname from tvshows where genres="+tvgenre+"and languages="+tvlanguages
    cur.execute(str_tvn)
    tv=cur.fetchall()
    st.text("TV SHOW NAME:")
    for i in tv:
        for j in i:
            st.text(j)
    #GETTING IMDB RATING
    tv_i="select imdb from tvshows where genres="+tvgenre+"and languages="+tvlanguages
    cur.execute(tv_i)
    mov4=cur.fetchall()
    st.text("IMDB RATING:")
    for i in mov4:
        for j in i:
            st.text(j)

    cpass="'Phone'"
    phone=0000000000
    cname="'Name'"
    dob="'01jan03'"

    st.header("Create New Account:")
    cname=st.text_input("Enter Name: ")
    #names.append(cname)
    cpass=st.text_input("Enter Password:")
    passwords.append(cpass)
    phone=st.text_input("Enter Phone: ")
    dob=st.text_input("Enter Date of Birth: ")
    plan=["Select Plan","'Mobile'","'Basic'","'Standard'","'Premium'"]
    plan_input=st.selectbox('Plan:',plan)
    paymethod=["Select Method of Payment","'Debit Card'","'Credit Card'","'UPI'","'Net Banking'"]
    paymethod_input=st.selectbox('Method of Payment:',paymethod)

    cur.execute("select custid from customer order by custid desc limit 1")
    custID=cur.fetchall()
    for i in custID:
        for j in i:
            new_custID=j+1
    usernames.append(new_custID)
    if(st.button('SUBMIT')):        
        cur.execute("insert into customer (phone, name1, custid, dob) values (%s, %s, %s, %s)", (phone, cname, new_custID, dob))
        conn.commit()
        st.title(":white_check_mark: New Account has been created!")
        st.text("Username for your new account is:")
        st.text(new_custID)

    
    #CONTACT FORM
    st.header(":mailbox: Request for your payment details here!")

    contact_form="""
        <form action="https://formsubmit.co/21pt25@psgtech.ac.in" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here:"></textarea>
        <button type="submit">Send</button>
        </form>
        """

    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("C:\\Users\\HP\\style\\style.css.txt")


cur.close()
conn.close()