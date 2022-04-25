import streamlit as st 
from multipage import MultiApp
from PIL import Image
#calling the files from the apps folder
from apps2 import (
    stat2,
    accept2,
    tryAccept2
    )


apps = MultiApp()

#This application is used to demonstrate the untapped potential within the FDP
#communitites globally and the potentially positive effect from harnessing it,
#upon the consistant UNHCR funding gaps which is directly tied to the livelihood of the FDPs world wide. 


st.markdown(
    """The Dummy UNHCR FDP (Skills Predictive Evaluation) Prediction Application
     
    """
)

#Adding the applications

apps.add_app("Synthetic FDP re-employement data", stat2.app)
apps.add_app("FDP re-employement Scheme Selection", accept2.app)
apps.add_app("Predictive Contribution Ranage", tryAccept2.app)

#The main application page
apps.run()