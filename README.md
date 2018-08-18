# terencehagans.github.io

<!DOCTYPE html>
<html>


<head>
    <meta charset="utf-8">
    <title>Your first HTML form, styled</title>
    <style>
      form {
        /* Just to center the form on the page */
        margin: 0 auto;
        width: 400px;
        /* To see the outline of the form */
        padding: 1em;
        border: 1px solid #CCC;
        border-radius: 1em;
      }
      form div + div {
        margin-top: 1em;
      }
      label {
        /* To make sure that all labels have the same size and are properly aligned */
        display: inline-block;
        width: 90px;
        text-align: right;
      }
      input, textarea {
        /* To make sure that all text fields have the same font settings By default, textareas have a monospace font */
        font: 1em sans-serif;
        /* To give the same size to all text fields */
        width: 300px;
        box-sizing: border-box; /* To harmonize the look & feel of text field border */
        border: 1px solid #999;
      }
      input:focus, textarea:focus {
        /* To give a little highlight on active elements */
        border-color: #000;
      }
      textarea {
        /* To properly align multiline text fields with their labels */
        vertical-align: top;
        /* To give enough room to type some text */
        height: 5em;
      }
      .button {
        /* To position the buttons to the same position of the text fields */
        padding-left: 90px;
        /* same size as the label elements */
      }
      button {
        /* This extra margin represent roughly the same space as the space between the labels and their text fields */
        margin-left: .5em;
      }
    </style>
</head>




<body>

<h1>My First Heading</h1>

<iframe width="560" height="315" src="https://www.youtube.com/embed/hQ2vQkhK15k" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

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


<script src="https://checkout.stripe.com/checkout.js"></script>

<button id="customButton">Purchase</button>

<script>
var handler = StripeCheckout.configure({
  key: 'pk_test_CbIPmJVZ0QX4fknCtPRGAwLD',
  image: 'https://stripe.com/img/documentation/checkout/marketplace.png',
  locale: 'auto',
  token: function(token) {
    // You can access the token ID with `token.id`.
    // Get the token ID to your server-side code for use.
  }
});

document.getElementById('customButton').addEventListener('click', function(e) {
  // Open Checkout with further options:
  handler.open({
    name: 'ROAMD, LLC',
    description: '2 widgets',
    amount: 2000
  });
  e.preventDefault();
});

// Close Checkout on page navigation:
window.addEventListener('popstate', function() {
  handler.close();
});
</script>

<br>
<br>
<br>

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



<br>
<br>



<br>
<br>

<p>My first paragraph.</p>

</body>
</html>
