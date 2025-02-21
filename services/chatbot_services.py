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
    