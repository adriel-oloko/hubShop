{{meta}}
		
		<title>HUB || Login</title>
{{header}}

			<br />
			<br />
<div style="margin: auto; padding: width: 100%; height: auto; ">
			<div style="width: 70%; height: auto; border: 0px solid #00182B; margin: auto; border-radius: 25px; box-shadow: 0px 0px 14px #00182B; background: #F3F0F0; ">
				<div style="width: 100%; height: auto; margin: auto; margin-bottom: 45px;">	
				<div style="margin: auto; border-radius: 50%; border: 1px solid #010070; width: 40px; height: 40px;position: relative; top: 15px; background: #fff; box-shadow: 0px 0px 10px #001895; padding: 13px;">
				<img src="./images/logo.png" style="width: 100%;height:auto;">				<br />
				</div>
				</div>
				
				<hr />
				<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">Login</h4>
				<div style="width: 80%; height: auto; margin: auto;">
				<form action="/login" method="post" enctype="multipart/form-data">
				<input name = "email" type="text" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 10px;" placeholder="Email" />
					<input name="password" type="password" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 10px;" placeholder="Password" />
					<input value="Submit" type="submit" style="width: 50%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px;outline: none;" />
					<a href="/forgot-password" style="float: right; width: 30%; height: 30px; margin: auto; margin-bottom: 10px; font-size: 10px;">Forgotten password?</a>
					</form>
					
					<hr />
					<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">OR</h4>
						<a href="/register"><input type="submit" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px; outline: none;" value="Register"/></a>						<br /><br />				</div>
				</div>			</div>
		</div>
			
		
		<br /><br />
{{footer}}
<p>©{{yr}}</p>
			<br />
		</div>
	</body>
</html>