import os  
from dotenv import load_dotenv
from openai import AzureOpenAI  
import fitz

load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("OPENAI_API_VERSION") 
deployment = os.getenv("DEPLOYMENT_NAME")

client = AzureOpenAI(  
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint,   
)   

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        full_text += text + "\n"
    return full_text

def extract_resume(text):
    response = client.chat.completions.create(
        model=deployment,
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,
        messages=[
            {
                "role": "system",
                "content": """

                    You are an AI assistant that extracts information from resumes.
                    Extract the following information from the resume:
                    - University Name
                    - Degree
                    - Major
                    - CGPA
                    - Skills
                    - Work Experience
                    - Projects and its description (make the projects the header, then the description of the project as the bullet points)
                    - Certifications
                    - Achievements
                    
                    If some of the information is not available, just leave it blank, and skip the field, and put "None".
                    """
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    extracted_info = response.choices[0].message.content
    return extracted_info

def get_response(extracted_info, user_input):
    response = client.chat.completions.create(
        model=deployment,
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,
        messages=[
            {
                "role": "system",
                "content": f"""
                    You are a professional career advisor and writing assistant.

                    Write a personalized cover letter based on the following:

                    - Name: {user_input['name']}
                    - Email: {user_input['email']}
                    - Phone Number: {user_input['phone_number']}
                    - Address: {user_input['city']}, {user_input['state']}, {user_input['zip_code']}
                    - Job Title: {user_input['job_title']}
                    - Company: {user_input['company_name']}
                    - Job Description: {user_input['job_description']}
                    - Years of Experience: {user_input['years_of_experience']}
                    - Tone: {user_input['tone']}

                    Structure it with an engaging opening, tailored middle paragraphs, and a confident closing. Be concise, professional, and impactful.

                    Make the cover letter based on the years of experience, cater the creation of the cover letter for it to be 
                    suitable based on the year of experience and the job description provided.
                    
                    Make use of the extracted information from the resume as well:
                    {extracted_info}

                    The extracted information is to glorify the cover letter, and make it more appealing to the employer/hiring manager.
                    You do not have to make use all of the information, use if needed.

                    This is the most important information, use this format:

                    {user_input['name']} (in capital letters)
                    zip code, city (normal wording (with just the first letter capitalized)) like this: 10001, New York
                    state

                    Dear Hiring Manager,                                                 Date of the cover letter generated including the year (must be aligned with the Dear Hiring Manager, but at the far right side of the page)

                    APPLICATION FOR THE POSITION OF {user_input['job_title']} (in capital letters and must be underlined)

                    engaging opening paragraph

                    2. tailored middle paragraph (make sure to include the job description and the extracted information from the resume and tailor it to the job description) (keep the numbering 2., 3., 4., and so on if you have more than 4 paragraphs, and make sure to keep the numbering in the cover letter, without number 1.)

                    3. explain why you are best fit for the job, mainly explain your projects and achievements, and how it relates to the job description.

                    4. I am available for interview at your convenience and looking forward to hearing from your soon. I can be contacted at {user_input['phone_number']} and at the following email address: {user_input['email']}

                    Thank you in advance for your kind consideration,
                    Yours sincerely,

                    {user_input['name']} (in capital letters)
                    Degree, Major (normal wording (with just the first letter capitalized)) like this: Bachelor of Science, Computer Science
                    University Name (in capital letters)
                    {user_input['phone_number']}

                    """
            },
            {
                "role": "user",
                "content": str(user_input)
            }
        ]  
    )
    return response.choices[0].message.content
