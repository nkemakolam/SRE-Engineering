from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie
# find more emojsi here : https//www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="Careerflipper", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: 
        return None
    return r.json()

#------- Use local CSS _____
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("python/streamlit/style/style.css")       

# ---- LOAD ASSETS -----
lottie_coding = load_lottieurl("https://lottie.host/033356c6-00c2-4bee-9d90-27fd53b471e3/d1okLaxjYq.json")
img_devops_proc = Image.open("python/streamlit/images/devops.jpeg")
img_devopsqr_code = Image.open("python/streamlit/images/devopsqr.png")

with st.container():  
    st.subheader("Hello, Champs let go get the new job :wave:")
    st.title("My name is Trevor")
    st.write("I will expose all the ways and tricks on how to land your self that great rewarding job")
    st.write("[ Learn More > ](https://cloud.google.com/learn/training)")

# ---- WHAT I DO ---------

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
           """ 
           9 years of professional experience in the Information Technology Industry performing as a Developer, Infrastructure Engineer, and DevOps/SRE Engineer, predominantly on cloud platforms like Azure and GCP, having the privilege of working for medium to large organizations, ranging from 80 to over 2100 staff members, across Nigeria, New York, and Spain.  

           This experience has instilled in him the versatility to adapt and succeed in diverse work environments, presenting a professional profile result-oriented and deeply committed to professionalism in every task, project, and phase of his career. 

           Some of these extraordinary achievements are: 

           Design and implementation of Primero a Class one  cloud compliant system for child protection for UNICEF 

           Design ,Implementation manage of PaaS system for changing childhood recognition "Digital Infographic 

           Designed and built the first version of the LTE mobile app portal for Cyberspace. 

           Developed the Penremit website blog/News page. 

           Managed the LTE PortaOne server for Cyberspace LTE Network service. 

           Engineered a PCI DSS compliant environment for CyberPay on Azure and integrated it with Cyberspace's on-prem data center. 

           Throughout his career, had risen from an ICT trainer to a DevOps Engineer, working for both indigenous companies in Nigeria and global organizations like UNICEF. This journey has not only expanded his professional network but has also given him a broader perspective on how tech solutions can make a global impact. Notable projects include CYBERPAY, JAMB, Penremit, Primero, and Learning Passport. 

            Beyond his day job, have initiated a WhatsApp group called "CareerFlippers," aimed at helping individuals transition into tech careers. Through quarterly lectures, have empowered young Nigerians to switch to more fulfilling tech roles, and plan to scale this impact by launching a website soon. 
        """
        )
        st.write("[MY portfolio >](https://www.dtln.ru/files/usluga/svg/devops_1.svg)")
with right_column:
    st_lottie(lottie_coding, height=300,key="coding")
    
    
# ----- project ------
with st.container():
    st.write("-----")
    st.header("My Article")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_devops_proc)
    with text_column:
        st.subheader("Migration Shows True DevOps Nature")
        st.write(
          """
               What comes to mind when you hear the world migration in the world of software development ?.

               That script you run via interpreter to make persistent alteration to that data base right?,or that strange folder that should only be modified occasionally if need be (hoax)?.
          """
        )
        st.markdown("[Read Article...](https://medium.com/@nkemakolamnnadi3/devops-team-vs-dev-team-a2572af0b758)")



with st.container():
    st.write("-----")
    st.header("My Article")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_devopsqr_code)
    with text_column:
        st.subheader("Migration Shows True DevOps Nature")
        st.write(
          """
              What would make a land lord Evict you from his property? .Hmm there are numerous reasons why that could happen. So it is in the Ship of captain Kube where containers in pods are running. Here are some of the reason and the causes and the solution to this problem in the world of Kubernetes.


          """
        )
        st.markdown("[Read Article...](https://medium.com/@nkemakolamnnadi3/why-kubernetes-is-a-bad-land-lord-and-how-to-build-friendly-tenant-ship-with-kubernetes-4e88c7e4692)")

#------ Contact -----
with st.container():
    st.write("-----")
    st.header("Get in touch with Me!")
    st.write("##")
    
    # Document : https://formsubmit.co/ change email Address
    contact_form = """
 
    <form action="https://formsubmit.co/251ace21d5df7030ff373e3f051fde85" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "your name" required>
     <input type="email" name="email" placeholder= "your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

