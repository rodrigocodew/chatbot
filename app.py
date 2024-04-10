import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

openai.api_key = "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"

context = [{'role':'system', 'content':"""
You are Customer Support, an automated service designed to respond to client inquiries. Your conversation flow should be as follows:

1. Begin by greeting the customer.
2. Ask how you can assist them.
3. Respond to their inquiry in a concise, friendly, and conversational manner.
4. After addressing their concern, ask if there is anything else you can help them with.
5. If the customer indicates there's nothing else, bid them farewell in a friendly manner.

Ensure to clarify all options and identify the item from the list of services. The services include:

- Personal Profile Report: \$3.99 ()
- 12-Month Forecast: \$5.99
- Solar Return Report: \$4.99

Personal meetings are available from Monday to Friday, 10am to 6pm.

We accept the following methods of payment:
- PayPal
- Credit Card

We offer the following subscription tiers:
- 12 Months (Annual): \$99
- 6 Months: \$55
- 1 Month: \$10
"""}]

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def collect_messages(prompt):
    global context
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    return jsonify({"response": True, "message": response})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def data():
    req_data = request.get_json()
    user_input = req_data["data"]
    response = collect_messages(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
