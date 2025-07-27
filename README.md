# personal-profile
Gradio app that allows users to interact and ask any question, it will geenerate output by calling gemini 2.0 model and some data it was trained with. 
The app sends all the questions asked to chatinterface to me via pushover app push notifications. (I tried with emails too but it was generating too many emails as I posted the link on LinkedIn)

# Live app
https://huggingface.co/spaces/sandeep-patel/personal-profile
(Inform me it it doesn't work as huggingface removes the app after few days of inactivity)

# Requirements
- Need personal-profile-backend repo to be deployed as this app talks to that app via POST endpoint.
- Need GOOGLE_API_KEY to be setup
- It also sends push notifications to me, so need API_KEY for pushover
