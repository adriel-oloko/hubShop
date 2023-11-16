{{meta}}

	<title>HUB || Cart</title>

{{header}}

	<br />

	<center><h2 style="font-family: 'Nunito', sans-serif;">Cart <i id="icon-cart" class="fa fa-shopping-cart"></i></h2></center>

	<div id="main">

 		<div class="post">

		{% for entry in crt %}

			<table style="width: 100%; padding-right: 10px;">
			<tr>
				<th style="width: 30%;">
					<img src="/post/images/{{entry[5]}}" style=" height: auto; border: 0px solid #aaa;"/>
				</th>

				<th style="width: 60%;">
					<b><p style="padding-left: 10px; font-family: 'Nunito', sans-serif; text-align: left;">{{entry[3]}} - {{entry[4]}}  (×{{entry[6]}})<br /><br />₦{{entry[7]}}</p></b>
				</th>

				<th style="width: 10%; text-align: center;">
					<a href="/del-cart/{{entry[0]}}"><button style="border: 1px solid black; padding: 4px; width: 25px; height: 25px; border-radius: 100%; text-align: center;"><i class="fa fa-times"></i></button></a>
				</th>
			</tr>
		</table>

		<hr />

		{% endfor %}

		<h3 style="text-align: left;font-family: 'Nunito', sans-serif;">Total: ₦{{fmt_sum}}</h3>


	</div>

	<br />

	<script src="https://checkout.flutterwave.com/v3.js"></script>
	<table style="border: 0px solid #000; width: 100%;">
		<tr>
			<th style="display: none; border: 0px solid #000;">
				<button style="padding, 7px; border:1px solid #00182B; width: 100%; border-radius: 8px; background-color: #00182B; "font-family: 'Nunito', sans-serif; color: gold;" onClick="fiat()"><p style="color: gold; line-height: .5px;">Checkout with fiat</p></button>
			</th>

			<th style="border: 0px solid #000;">
				<a href="/card/checkout"><button style="padding, 7px; border:1px solid #00182B; width: 100%; border-radius: 8px; background-color: #00182B; "font-family: 'Nunito', sans-serif; color: gold;"><p style="color: gold; line-height: .5px; font-weight: 400; font-size: 18px;">Checkout with Card</p></button></a>
			</th>
		</tr>
	</table>

</div>
<br /><br />
{{footer}}
<p>©{{yr}}</p>
			<br />
		</div>


		<script>
			function fiat() {
				FlutterwaveCheckout({
				public_key: "FLWPUBK_TEST-a10ab8dad41aa2c9576d56752fcadb9d-X",
				tx_ref: "RX1",
				amount: {{sum}},
				currency: "NGN", country: "NG",
				payment_options: "card, mobilemoneyghana, ussd",
				redirect_url: "/bac/flutter/validate",
				meta: {
					consumer_id: {{u_data[0]}},

				},
				customer: {
					email: "{{u_data[3]}}",
					phone_number: "{{u_data[4]}}",
					name: "{{u_data[1]}} " + "{{u_data[2]}}"
			 },
			 callback: function (data) {
			 		console.log(data);
			 	},

			 	onclose: function() {
			 		// close modal
			 	},
			 	customizations: {
			 		title: "My store",
			 		description: "Payment for items in cart",
			 		logo: "http://localhost:8080/images/logo.png",
			 },
		 });
	 }
	 </script>
	</body>
</html>