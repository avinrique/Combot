
from datetime import date
import pandas as pd
import google.generativeai as genai
from time import sleep

# Configure genai and check available models
genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
model = genai.GenerativeModel("gemini-1.5-flash")


myfile = genai.upload_file("sad.jpg")
# print(f"{myfile=}")
result = model.generate_content(
    [myfile, "\n\n", "Can you tell me what is in the mood / emotion oof the guy of the guy in the picture netural happy sad confused or somethuing ?"]
)
print(f"{result.text=}")