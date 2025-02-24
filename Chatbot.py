import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDoSpeRzmjqnVhX4VEonfxpd6ZQzsceHNE")

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction=" Tax assistant that can automate tax filing processes, simplifying complex calculations, identifying deductions, and minimizing errors. Answer should be step by step.Maximum of 5 steps can be given.",
)

chat_session = model.start_chat(
  history=[
  ]
)

resp=input("Enter your query:")
response = chat_session.send_message(resp)

print(response.text)
