{{meta}}

		<title>HUB || Forgot password - OTP</title>
{{header}}

			<br />
			<br />
<div style="margin: auto; width: 100%; height: auto; ">
			<div style="width: 70%; height: auto; border: 0px solid #00182B; margin: auto; border-radius: 25px; box-shadow: 0px 0px 14px #00182B; background: #F3F0F0; ">
				<div style="width: 100%; height: auto; margin: auto; margin-bottom: 45px;">
				<div style="margin: auto; border-radius: 50%; border: 1px solid #010070; width: 40px; height: 40px;position: relative; top: 15px; background: #fff; box-shadow: 0px 0px 10px #001895; padding: 13px;">
				<img src="./images/logo.png" style="width: 100%;height:auto;">				<br />
				</div>
				</div>

				<hr />
				<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">OTP</h4>
				<div style="width: 80%; height: auto; margin: auto;">

				<form action="/forgot-password-validate" method="post" enctype="multipart/form-data">

				<input name = "email" type="text" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 0px;outline: none; padding-left: 10px;" value="{{email}}" placeholder="Email" disabled/>

				<input name = "email" type="text" style="visibility: hidden; height: 0px; margin: -20px; padding: 0px;" value="{{email}}" placeholder="Email" />

					<input name="password" type="password" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 0px;outline: none; padding-left: 10px;" value="{{password}}" placeholder="Password" disabled/>

					<input name="password" type="password" style="visibility: hidden; height: 0px; margin: -20px; padding: 0px;" value="{{password}}" placeholder="Password" />

					<input name="otp" type="number" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 10px;" placeholder="OTP"/>

					<input value="Submit" type="submit" style="width: 50%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px;outline: none;" />

					</form>

					<br />
				</div>
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