#import sendgrid
#from sendgrid.helpers.mail import Mail
import resend
import os
import program

# Replace with your actual API key
#SENDGRID_API_KEY = "re_bG1tMRjQ_GHULKZJKx422sUM5P5Yjsxaf" 
resend.api_key = "re_bG1tMRjQ_GHULKZJKx422sUM5P5Yjsxaf" #os.environ["RESEND_API_KEY"]

f: bytes = open(
  os.path.join(os.path.dirname(__file__), "static/sample.pdf"), "rb"
).read()

attachment: resend.Attachment = {"content": list(f), "filename": "sample.pdf"}

def send_email(to_email, subject, content):
    # message = Mail(
    #     from_email='Acme <ahmed@tahermedicalconsultancy.com>', # Replace with your sender email
    #     to_emails=to_email,
    #     subject=subject,
    #     html_content=content
    # )
    
    pdfFile = program.PdfGen()
    pdfFile.createPdf()

    params: resend.Emails.SendParams = {
        "from": "Metamorphic.fit <ahmed@tahermedicalconsultancy.com>",
        "to": ["ahmed.sowdagar@gmail.com","1993.ksk@gmail.com"],
        "subject": "Hello Metamorphic",
        "html": "<strong>This is a test email sent from Silicon bay consulting on behalf of Metamorphic.fit. Testing the email poc</strong>",
        "attachments": [attachment]
    }

    try:
        #sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
        email = resend.Emails.send(params)
        print(email)
        #response = sg.send(message)
        #print(f"Email sent to {to_email} with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email {e}")

if __name__ == '__main__':
#     recipient_email = 'ahmed.sowdagar@gmail.com' # Replace with recipient email
#     email_subject = 'Test Email from SendGrid'
#     email_content = '<p>Hello, this is a test email sent using SendGrid and Python.</p>'
      send_email('','','')