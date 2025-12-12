from django.shortcuts import render
from .models import Project   # <-- add the Project model
from .forms import ContactForm
from django.core.mail import send_mail

# About page
def about_view(request):
    return render(request, 'pages/about_me.html')

# Experience page
def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    #Handle contact form submission
    if request.method =='POST':
        form = ContactForm(request.POST)

        #Validate the form and collect the data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            

            #build email content
            message_body = (
                f'You have a new Email from your portfolio Webpage \n'
                f'Name : {name} \n'
                f'Email : {email} \n'
                f'Message : {message} \n'
            )
            try:
                send_mail(
                    #Subject
                    f'Email Form Portfolio Website',
                    #Message Body ---> The user typed message
                    message_body,
                    email, #from Email user Email
                    ['timterrance.tech@gmail.com'] # To: Where you want to receive the email
                )
                #after sending the email, 
                form = ContactForm() # reset the form
                return render(request, 'pages/contact.html', {'form': form,}) 
            #If there is an error sending the email
            except Exception as e:
                print(f'Error sending email:{e}')
                return render (request, 'pages/contact.html', {'form': form})
            
        else:
            print('Form is no valid')
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

