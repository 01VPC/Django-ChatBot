from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import os
api_key='AIzaSyBJPF1ORxWVbANg7VLAohPFcHEQd2p2c-U'

def ask_openai(message):
    genai.configure(api_key='AIzaSyBJPF1ORxWVbANg7VLAohPFcHEQd2p2c-U')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(message)
    text = response.candidates[0].content.parts[0].text

    print(text)
    return text
    
    # if model.choices[0].message!=None:
    #     return model.choices[0].message


# Create your views here
def chatbot(request):
    if request.method == 'POST' :
        message=request.POST.get('message')
        response= ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

# api_key = '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'
# openai.api_key= api_key

# def ask_openai(message):
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an helpful assistant."},
#             {"role": "user", "content": message},
#         ]
#     )
    
#     answer = response.choices[0].message.content.strip()
#     return answer

# def ask_openai(message):
#     stream = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "Say this is a test"}],
#         stream=True,
#     )
#     for chunk in stream:
#         if chunk.choices[0].delta.content is not None:
#             answer=chunk.choices[0].delta.content
#             print(chunk.choices[0].delta.content, end="")
#             return answer