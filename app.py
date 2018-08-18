from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <br />
    <br />
    <br />

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hQ2vQkhK15k" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

    <br />
    <br />
    <br />
    
    <form action="/my-handling-form-page" method="post">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" name="user_name">
      </div>
      <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail" name="user_mail">
      </div>
      <div>
        <label for="msg">Message:</label>
        <textarea id="msg" name="user_message"></textarea>
      </div>
    </form>


    <br />
    <br />


    <form action="your-server-side-code" method="POST">
      <script
        src="https://checkout.stripe.com/checkout.js" class="stripe-button"
        data-key="pk_test_CbIPmJVZ0QX4fknCtPRGAwLD"
        data-amount="999"
        data-name="ROAMD, LLC"
        data-description="Widget"
        data-image="https://stripe.com/img/documentation/checkout/marketplace.png"
        data-locale="auto">
      </script>
    </form>





    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
