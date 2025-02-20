# app/chatbot_routes.py

from fastapi import APIRouter, HTTPException
from services.chatbot_services import (
    
    select_lang_service,
    select_type_service,
    extract_name_service,
    time_slot_service
)

router = APIRouter()

# ---------------------------
# 1. Welcome & Language Selection
# ---------------------------

@router.get("/welcome")
async def welcome():
    return {"message": welcome_service()}

@router.post("/select_lang")
async def select_language(user_input: dict):
    language = select_lang_service(user_input)
    return {"selected_language": language}

@router.post("/select_type")
async def select_type(user_input: dict):
    type = select_type_service(user_input)
    return {"selected_service": type}

@router.post("/extract_name")
async def extract_name(user_input: dict):
    extracted_name = extract_name_service(user_input)
    return {"name": extracted_name}



@router.post("/time_slot")
async def time_slot(user_input: dict):
    time = time_slot_service(user_input)
    return {"slot": time}

# 3. Check-In Workflow
# ---------------------------

@router.get("/check_in_1")
async def check_in_1():
    return {"message": check_in_1_service()}



@router.post("/order_confirm")
async def confirm_order(user_input: dict):
    response = confirm_order_service(user_input)
    return {"confirmation": response}

@router.post("/payment")
async def payment(user_input: dict):
    response = payment_service(user_input)
    return {"payment": response}



@router.get("/confirm_appointment")
async def confirm_appointment():
    return {"message": confirm_appointment_service()}

# ---------------------------
# 4. Walk-In Workflow
# ---------------------------

@router.get("/walk_in")
async def walk_in():
    return {"message": walk_in_service()}

@router.post("/select_consultation")
async def select_consultation(user_input: dict):
    consultation = select_consultation_service(user_input)
    return {"selected_consultation": consultation}

@router.get("/doctors")
async def doctors():
    return {"message": doctors_service()}

@router.post("/select_doctor")
async def select_doctor(user_input: dict):
    doctor_selection = select_doctor_service(user_input)
    return {"selected_doctor": doctor_selection}

# ---------------------------
# 5. Additional Walk-In Steps: Patient Registration, Payment, and Token Generation
# ---------------------------

@router.post("/register_patient")
async def register_patient(user_input: dict):
    """Register a new walk-in patient with basic information."""
    registration_status = register_patient_service(user_input)
    return {"registration_status": registration_status}

@router.post("/process_payment")
async def process_payment(user_input: dict):
    """Process the payment for a walk-in consultation."""
    payment_status = payment_service(user_input)
    return {"payment_status": payment_status}

@router.get("/generate_token")
async def generate_token():
    """Generate a token number for the walk-in patient to be called when their turn arrives."""
    token_info = generate_token_service()
    return {"token_details": token_info}
