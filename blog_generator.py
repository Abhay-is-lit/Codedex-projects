from google import genai


# Setting up API key.

client = genai.Client(api_key="AIzaSyAqW-cCX8EHiesav9YeDbAJBTxuumwGBIk")

generation_config = genai.types.GenerationConfig(
    max_output_tokens=67
)
# ---- ----- ---- ---- ----- ----- ----- ----- ----- ----- ----- ------ 

# Promt
work = input("Want me to write someting on any topic? (y/n) :     ")



if work.lower() == 'y':
    prompt = input("What's on your mind? :")
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents= prompt
    )
    print(response.text)
else:
    print("Okay, see you later!")


