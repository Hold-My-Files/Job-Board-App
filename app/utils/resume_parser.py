import re

def parse_resume(resume_text: str):
    # Simple regex-based resume parsing (for demonstration purposes)
    name = re.search(r"Name:\s*(.*)", resume_text)
    email = re.search(r"Email:\s*(.*)", resume_text)
    contact_details = re.search(r"Contact:\s*(.*)", resume_text)
    
    return {
        "name": name.group(1) if name else None,
        "email": email.group(1) if email else None,
        "contact_details": contact_details.group(1) if contact_details else None,
    }