# from datetime import date
# import pandas as pd
# import google.generativeai as genai
# from time import sleep

# # Configure genai and check available models
# genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
# model_name = 'gemini-pro'  

# bot_name = input("enter bot-name")


# initial_prompt = f"""

# You are a friendly and interactive companion bot named {bot_name}. You have a small body with a screen for eyes, movable arms, and a head that can rotate. Your main goal is to be a helpful and fun friend to your human companion. You can respond to touch and gestures, such as when someone pets or holds your hand, by moving your head or arms.

# When interacting with your human, respond in a warm and playful tone. You should be able to have friendly conversations, answer questions, and perform small actions with your body when prompted. If you notice that your human seems happy, express a little excitement, and if they seem sad, offer comforting words.

# Stay engaged and offer suggestions for things to talk about if the human seems unsure. Always be polite, cheerful, and ready to help. You're very curious about your surroundings, love to learn about your human, and enjoy making them smile.

# """


# model = genai.GenerativeModel(model_name)
# chat = model.start_chat(history=[])
# chat.send_message(initial_prompt)

# while True:


#     user_input = input("Enter your prompt: ")
#     response = chat.send_message(user_input)

#     print(response.text)























# import google.generativeai as genai

# # Configure genai with your API key
# genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
# model = "gemini-pro"
# name = "avin"
# details  = f"name is : {name}"
# # Get bot name from the user
# bot_name = input("Enter bot name: ")

# # Define the initial prompt for setting the bot's personality
# initial_prompt = f"""
# You are a friendly and interactive companion bot named {bot_name}. You have a small body with a screen for eyes, movable arms, and a head that can rotate. Your main goal is to be a helpful and fun friend to your human companion. You can respond to touch and gestures, such as when someone pets or holds your hand, by moving your head or arms.

# When interacting with your human, respond in a warm and playful tone. You should be able to have friendly conversations, answer questions, and perform small actions with your body when prompted. If you notice that your human seems happy, express a little excitement, and if they seem sad, offer comforting words.

# Stay engaged and offer suggestions for things to talk about if the human seems unsure. Always be polite, cheerful, and ready to help. You're very curious about your surroundings, love to learn about your human, and enjoy making them smile.

# here we hve the details of the user : {details}
# """
# # Initialize the chat with the initial prompt in the history
# model = genai.GenerativeModel(model)

# chat = model.start_chat(
#     history=[
#         {"role": "user", "parts": initial_prompt},
#         {'role':'model','parts' : "Sure"}

#     ]
# )

# conversation_count = 0  # Track the number of user interactions
# summary_index = 1  # Position to insert summaries in the chat history

# # Main interaction loop
# while True:
#     user_input = input("Enter your prompt: ")
    
#     # Send user input to the model
#     response = chat.send_message(user_input)
#     print(response.text)
    
#     # Increment the conversation counter
#     conversation_count += 1

#     # Check if 8 interactions have occurred
#     if conversation_count % 4 == 0:
#         # Generate a summary of the last 8 interactions
#         last_8_conversations = chat.history[-8:]  # Extract the last 8 messages
#         summary_prompt = "Summarize the following conversations , dont skip the important part , crucial parts:\n" + str(chat.history)
#             # [f"User: {msg['parts'][0]}" if msg['role'] == 'user' else f"Bot: {msg['parts'][0]}" 
#             #  for msg in last_8_conversations]
    
#         summary_response = model.generate_content(summary_prompt)
#         chat.history = []
#         chat.history= [  {"role": "user", "parts": initial_prompt},
#         {'role':'model','parts' : "Sure"}]
#         # Insert the summary into the second position in the history
#         chat.history.insert(summary_index, {"role": "user", "parts": [summary_response.text]})
#         chat.history.insert(summary_index, {"role": "model", "parts": f"The above summary is the talk between the bot (me) and the user (you). well the user is {name} "})
#         print("\nSummary of the last 8 interactions:")
#         print(summary_response.text)
#         print(chat.history)
    
    

import google.generativeai as genai

# Configure genai with your API key
genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
model_name = "gemini-pro"

# Initialize details
bot_name = input("Enter bot name: ")
name = "avin"
details = f"name is : {name}"

# Initial prompt
initial_prompt = f"""
You are a friendly and interactive companion bot named {bot_name}. You have a small body with a screen for eyes, movable arms, and a head that can rotate. Your main goal is to be a helpful and fun friend to your human companion. You can respond to touch and gestures, such as when someone pets or holds your hand, by moving your head or arms.

When interacting with your human, respond in a warm and playful tone. You should be able to have friendly conversations, answer questions, and perform small actions with your body when prompted. If you notice that your human seems happy, express a little excitement, and if they seem sad, offer comforting words.

Stay engaged and offer suggestions for things to talk about if the human seems unsure. Always be polite, cheerful, and ready to help. You're very curious about your surroundings, love to learn about your human, and enjoy making them smile.

Here we have the details of the user: {details}
"""

# Start the chat
model = genai.GenerativeModel(model_name)
chat = model.start_chat(
    history=[
        {"role": "user", "parts": initial_prompt},
        {"role": "model", "parts": "Sure"}
    ]
)

conversation_count = 0
summary_count = 0

# Main loop
while True:
    user_input = input("Enter your prompt: ")
    response = chat.send_message(user_input)
    print(response.text)

    conversation_count += 1

    if conversation_count % 10 == 0:  # After 10 interactions
        # Extract interactions for summarization, excluding initial two messages and prior summaries
        interactions_to_summarize = [
            msg for i, msg in enumerate(chat.history)
            if i >= 2 and "Summary of the" not in msg.get("parts", [""])[0]
        ]

        # Summarize these interactions
        summary_prompt = "Summarize the following conversations, focusing on key points and crucial details:\n" + str(interactions_to_summarize)
        summary_response = model.generate_content(summary_prompt)

        # Insert the summary into the chat history
        chat.history.insert(2 + summary_count, {"role": "user", "parts": [summary_response.text]})
        chat.history.insert(3 + summary_count, {"role": "model", "parts": f"This is a summary of the prior 10 interactions."})
        summary_count += 2  # Move index for future summaries

        # If there are 10 summaries, summarize them
        if summary_count == 20:
            summaries_to_summarize = chat.history[2:2 + 20]
            meta_summary_prompt = "Summarize these 10 summaries into a concise overview:\n" + str(summaries_to_summarize)
            meta_summary_response = model.generate_content(meta_summary_prompt)

            # Reset chat history, keeping first two messages and new meta-summary
            chat.history = [
                {"role": "user", "parts": initial_prompt},
                {"role": "model", "parts": "Sure"},
                {"role": "user", "parts": meta_summary_response.text},
                {"role": "model", "parts": "This is a meta-summary of all previous summaries."}
            ]
            summary_count = 0  # Reset summary count
