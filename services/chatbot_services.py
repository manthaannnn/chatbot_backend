# app/chatbot_services.py

from services.gemini1 import get_response_from_ai

# ---------------------------
# 1. Welcome & Language Selection
# ---------------------------

# def welcome_service():
#     return "Welcome to Our Hospital. I can speak with you in 3 languages: Hindi, English, and Kannada. Please select one language."

def select_lang_service(user_input):
    user_prompt = user_input['user_string']

    system_prompt = """
    You are an assistant that reads the user's prompt and selects one of the following languages. Just return the option number:
    1) Hindi
    2) English
    """

    response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)

    if "1" in response:
        return "Hindi"
    if "2" in response:
        return "English"
    return "Error"


def select_type_service(user_input):
    user_prompt = user_input['user_string']

    system_prompt = """
    You are an assistant that reads the user's prompt and selects one of the following options. Just return the option number:
    1. Step Digital 
    2. Step Production
    3. Step Tech
    """

    response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)

    if "1" in response:
        return "Digital"
    if "2" in response:
        return "Production"
    if "3" in response:
        return "Tech"
    return "Error"



def step_digital(user_input):
    user_prompt = user_input['user_string']

    # Simplified system prompt for matching quantities and pizza types
    system_prompt = """
    You are an assistant that reads the user's prompt and selects one of the following options. Just return the option number:
    1. Performance Marketing 
    2. Search Engine Optimisation 
    3. Social Media Management 

    """

    # Get AI response
    response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)
    if "1" in response:
        return "Performance Marketing"
    if "2" in response:
        return "Search Engine Optimisation"
    if "3" in response:
        return "Social Media Management"
    return "Error"
    # Return the formatted response

def step_production(user_input):
    user_prompt = user_input['user_string']
    system_prompt = """
    You are an assistant that reads the user's prompt and selects one of the following options for Step Production. Just return the option number:
    1. Video Production and shoot
    2. Ad shoot
    3. Video editing
    4. 3D graphics and animation
    5. Product and Fashion shoot
    """

    # Get AI response
    response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)
    if "1" in response:
        return "Video Production and shoot"
    elif "2" in response:
        return "Ad shoot"
    elif "3" in response:
        return "Video editing"
    elif "4" in response:
        return "3D graphics and animation"
    elif "5" in response:
        return "Product and Fashion shoot"
    return "Error"


def step_tech(user_input):
    user_prompt = user_input['user_string']
    system_prompt = """
    You are an assistant that reads the user's prompt and selects one of the following options for Step Tech. Just return the option number:
    1. Mobile or web app development
    2. Custom Software Development
    3. Data Analytics Service
    4. Automation Solutions
    """

    # Get AI response
    response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)
    if "1" in response:
        return "Mobile or web app development"
    elif "2" in response:
        return "Custom Software Development"
    elif "3" in response:
        return "Data Analytics Service"
    elif "4" in response:
        return "Automation Solutions"
    return "Error"

def extract_name_service(user_input):
    user_prompt=user_input['user_string']
    
    system_prompt="""
    you are an assistant that reads the user prompts and decides if user is saying yes or no .If user wants to say yes JUST RETURN "1" , If User wants to no say JUST RETURN "2" """
    
    response=get_response_from_ai(user_prompt=user_prompt,system_prompt=system_prompt)
    if "1" in response:
        return "Yes"
    elif "2" in response:
        return "No"
    return "Error"

def time_slot_service(user_input):
    user_prompt=user_input['user_string']
    
    system_prompt="""
    you are an assistant that reads the user prompts and decides if user is saying monday 10 am or tuesday 2pm .If user wants to say monday or 10 am JUST RETURN "1" , If User wants to say  tuesday or 2 pmJUST RETURN "2" """
    
    response=get_response_from_ai(user_prompt=user_prompt,system_prompt=system_prompt)
    if "1" in response:
        return "Mon"
    elif "2" in response:
        return "Tues"
    return "Error"
    

# def confirm_order_service(user_input):
#     user_prompt = user_input['user_string']

#     system_prompt = """
#     You are an assistant that reads the user's prompt and selects one of the following options. Just return the option number:
#     1) Yes confirm the order
#     2) i want to change the order
#     """

#     response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)

#     if "1" in response:
#         return "No Change"
#     if "2" in response:
#         return "Order Change"
#     return "Selection not recognized."


# def payment_service(user_input):
#     # Safely retrieve user input
#     user_prompt = user_input.get('user_string', '').strip()
#     if not user_prompt:
#         return "Invalid input: user_string is missing."

#     # Define system prompt
#     system_prompt = """
#     You are an assistant that determines the user's preferred payment method based on their input.
#     Respond with the corresponding number only:
#     1) UPI
#     2) Cash
#     3) Card
#     """

#     # Get response from AI
#     response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)

#     # Handle response
#     if response.strip() == "1":
#         return "UPI"
#     elif response.strip() == "2":
#         return "Cash"
#     elif response.strip() == "3":
#         return "Card"
#     else:
#         return "Payment method not recognized. Please specify UPI, Cash, or Card."

# def confirm_appointment_service():
#     return "Check your details and confirm the appointment."

# # ---------------------------
# # 4. Walk-In Workflow
# # ---------------------------

# def walk_in_service():
#     return """Let's book an appointment for you. 
#     We offer the following types of consultation:
#     1) Speciality OPD
#     2) General OPD
#     3) ENT OPD
#     4) Dentist OPD
#     """

# def select_consultation_service(user_input):
#     user_prompt = user_input['user_string']

#     system_prompt = """
#     You are an assistant that reads the user's prompt and selects one of the following options. Just return the option number:
#     1) Speciality OPD
#     2) General OPD
#     3) ENT OPD
#     4) Dentist OPD
#     """

#     response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)

#     consultations = {
#         "1": "Speciality OPD",
#         "2": "General OPD",
#         "3": "ENT OPD",
#         "4": "Dentist OPD"
#     }

#     return consultations.get(response.strip(), "Consultation type not recognized.")

# def doctors_service():
#     return """
#     Here are the available doctors and their schedules:
#     1) Dr. Smith - Available: Monday, 9:00 AM - 12:00 PM
#     2) Dr. Johnson - Available: Tuesday, 1:00 PM - 4:00 PM
#     3) Dr. Lee - Available: Wednesday, 10:00 AM - 1:00 PM
#     4) Dr. Patel - Available: Thursday, 11:00 AM - 2:00 PM
#     5) Dr. Brown - Available: Friday, 2:00 PM - 5:00 PM
#     """

# def select_doctor_service(user_input):
#     user_prompt = user_input['user_string']

#     system_prompt = """
#     You are an assistant that reads the user's prompt and selects one of the following doctors. Just return the option number:
#     1) Dr. Smith - Available: Monday, 9:00 AM - 12:00 PM
#     2) Dr. Johnson - Available: Tuesday, 1:00 PM - 4:00 PM
#     3) Dr. Lee - Available: Wednesday, 10:00 AM - 1:00 PM
#     4) Dr. Patel - Available: Thursday, 11:00 AM - 2:00 PM
#     5) Dr. Brown - Available: Friday, 2:00 PM - 5:00 PM
#     """

#     response = get_response_from_ai(user_prompt=user_prompt, system_prompt=system_prompt)

#     doctors = {
#         "1": {"name": "Dr. Smith", "schedule": "Monday, 9:00 AM - 12:00 PM"},
#         "2": {"name": "Dr. Johnson", "schedule": "Tuesday, 1:00 PM - 4:00 PM"},
#         "3": {"name": "Dr. Lee", "schedule": "Wednesday, 10:00 AM - 1:00 PM"},
#         "4": {"name": "Dr. Patel", "schedule": "Thursday, 11:00 AM - 2:00 PM"},
#         "5": {"name": "Dr. Brown", "schedule": "Friday, 2:00 PM - 5:00 PM"}
#     }

#     selected_doctor = doctors.get(response.strip())

#     if selected_doctor:
#         return f"Your selected doctor is {selected_doctor['name']}. They are available on {selected_doctor['schedule']}."
#     else:
#         return "Doctor selection not recognized. Please select a valid option."

# # ---------------------------
# # 5. Additional Walk-In Steps: Patient Registration, Payment, and Token Generation
# # ---------------------------

# def register_patient_service(user_input):
#     name = user_input.get('name')
#     age = user_input.get('age')
#     gender = user_input.get('gender')
#     return f"Patient {name}, Age: {age}, Gender: {gender} registered successfully. Please proceed to doctor selection."


# def generate_token_service():
#     return {
#         "token_number": "102",
#         "instructions": "Please wait for your token number to be called. Follow the signs to the waiting area."
#     }
