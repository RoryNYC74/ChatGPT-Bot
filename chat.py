from tkinter import *
import customtkinter
#import openai
import os
import pickle

#Iniate app
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry ('600x525')
#root.iconbitmap('ai_lt.ico') #I don't have the file

#Set color scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Submit to ChatGPT
from openai import OpenAI

def speak():
    if chat_entry.get():
        filename = "api_key"

        try:
            if os.path.isfile(filename):

                with open(filename, 'rb') as input_file:
                    stuff = pickle.load(input_file)

                my_text.insert(END, "Working...\n")

                # Create client properly
                client = OpenAI(api_key=stuff)

                # Send request
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=chat_entry.get()
                )

                # Extract text safely
                reply = response.output[0].content[0].text

                my_text.insert(END, reply)
                my_text.insert(END, "\n\n")

            else:
                with open(filename, 'wb'):
                    pass

                my_text.insert(
                    END,
                    "\n\nYou need an API key:\nhttps://platform.openai.com/api-keys"
                )

        except Exception as e:
            my_text.insert(END, f"\n\nThere was an error:\n{e}")

    else:
        my_text.insert(END, "\n\nYou forgot to type something.")

#Clear the screens
def clear():
	#Clear the Main Text box
	my_text.delete(1.0, END)

	#Clear the Entry widget
	chat_entry.delete(0, END)

#API inputs
def key():
	#Define our filename
	filename = "api_key"

	try:

		if os.path.isfile(filename):
			#Open the file
			input_file = open(filename, 'rb')
			
			#Load the data from the file into a varible
			stuff = pickle.load(input_file)
			
			#Output stuff to our entry box
			api_entry.insert(END, stuff)
		else: 
			#Create the file
			input_file = open(filename, 'wb')
			#Close the file
			input_file.close()
	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")

#Resize app larger
	root.geometry('600x650')
	#Reshow API frame
	api_frame.pack(pady=30)

#Save the API key
def save_key():
	#Define our filename
	filename = "api_key"

	try:
	
		#Open file
		output_file = open(filename, 'wb')
		
		#Add data to the file
		pickle.dump(api_entry.get(), output_file)

		#Delete Entry Box
		api_entry.delete(0, END)

		#Hide API frame
		api_frame.pack_forget()
		#Resize app smaller
		root.geometry('600x525')
	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")

#Create text frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

#Add text widget to get ChatGPT responses
my_text = Text(text_frame,
	bg="#343638",
	width=65,
	bd=1,
	fg="#d6d6d6",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d",
	selectforeground="#ffffff")

my_text.grid(row=0, column=0)

#Create scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

#Add scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)

#Entry widget to type info for ChatGPT
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type something to ChatGPT...",
	width=535,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

#Create button frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

#Create Submit Button
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak to ChatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

#Create Clear Button
clear_button = customtkinter.CTkButton(button_frame,
	text="Clear Response",
	command=clear)
clear_button.grid(row=0, column=1, padx=25)

#Create API Button
api_button = customtkinter.CTkButton(button_frame,
	text="Update API Key",
	command=key)
api_button.grid(row=0, column=2, padx=25)

#Add API key frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

#Add API entry widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter Your API Key",
	width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

#Add API button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save Key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)



root.mainloop()

exit()