# student_list is the list of students who are going to get shoutout.Initially it is empty which will get filled as per user's choice
student_list = []

# element_name is one who is going to get shoutout
element_name=input("Enter the name of someone whom you want to give shoutout:")
student_list.append(element_name)

while True:
    # new_element will ask if we want to add a new element to student_list
    new_element=input("Do you want to add someone for ShoutOut List? Enter 'Y' for yes and any other key for no:")
    # If value of new_element variable if "Y" then the loop will continue and ask for the element that is going to get shoutout
    if new_element.upper()=="Y":
        element_name=input("Enter the name of someone whom you want to give shoutout:")
        student_list.append(element_name)
    # If value of new_element variable isn't "Y" then the loop will get terminated
    else:
        break

# shoutout_message is the message that will contain the shoutout message for each and everyone
shoutout_message = ""
for student in student_list:
    shoutout_message = shoutout_message + f"Shoutout to {student}."

language="en"

from gtts import gTTS

shoutout_voice=gTTS(text=shoutout_message, lang=language, slow=False)
shoutout_voice.save("shoutout.mp3")