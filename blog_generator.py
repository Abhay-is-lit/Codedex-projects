from google import genai
from dotenv import dotenv_values

config = dotenv_values(".env")

# Setting up API key.

client = genai.Client()

generation_config = genai.types.GenerationConfig(
    max_output_tokens=50,
)
# ---- ----- ---- ---- ----- ----- ----- ----- ----- ----- ----- ------ 

# Promt
work = input("Want me to write someting on any topic? (y/n) :     ")



if work.lower() == 'y':
    prompt = input("What's on your mind? :")
    response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents= prompt+ "System instruction: Make the response consice and to the point. while keeeping it short and structured" 
    )
    print(response.text)
else:
    print("Okay, see you later!")


