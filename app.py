from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests
from forex import is_valid_currency, is_valid_amount, get_converted_amount

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.debug = True

toolbar = DebugToolbarExtension

@app.route('/')
def home_route():
    return render_template('home.html')

@app.route('/forex')
def forex_route():
    convertfrom = request.args.get('from_input', '')
    convertto = request.args.get('to_input', '')
    amount = request.args.get('amount_input', '')

    if not convertfrom or not convertto or not amount:
        None
    else: 
        if not is_valid_currency(convertfrom):
            flash('The length of your currency is invalid. Please use a valid 3-letter currency code for Convert From.')
        if not is_valid_currency(convertto):
            flash('The length of your currency is invalid. Please use a valid 3-letter currency code for Convert To.')
        if not is_valid_amount(amount):
            flash("Please enter a valid amount above 0")

    converted_amount, symbol = get_converted_amount(convertfrom, convertto, amount)

    symboled_amount = f"{symbol} {converted_amount}" if converted_amount is not None else None

    return render_template('forex.html', convertfrom=convertfrom, convertto=convertto, amount=amount, symboled_amount=symboled_amount)










# from flask import Flask, request, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
# import requests
# import forex

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "abc123"
# app.debug = True

# toolbar = DebugToolbarExtension

# @app.route('/')
# def home_route():
#     return render_template('home.html')

# @app.route('/forex')
# def forex_route():
#     convertfrom = request.args.get('from_input', '')
#     convertto = request.args.get('to_input', '')
#     amount = request.args.get('amount_input', '')

#     if len(convertfrom) != 3:
#         flash('The length of your currency is invalid. Please use a valid 3 letter currency index')
    
#     if len(convertto) != 3:
#         flash('The length of your currency is invalid. Please use a valid 3 letter currency index')
    
#     if amount < 0:
#         flash("Please enter an amount above 0. We don't calculate negatives.") 

#     if amount.value() == 0:
#         flash("Please enter a valid amount above 0") 

#     url = f'https://api.exchangerate.host/convert?from={convertfrom}&to={convertto}&amount={amount}'
#     response = requests.get(url)
#     data = response.json()

#     print(data)

#     converted_amount = data['result']

#     symbol = data['query']['to']

#     if converted_amount is not None:
#         converted_amount = round(converted_amount, 2)

#     symboled_amount = f"{symbol} {converted_amount}" if converted_amount is not None else None

#     print(symboled_amount)

#     return render_template('forex.html', convertfrom=convertfrom, convertto=convertto, amount=amount, symboled_amount=symboled_amount)