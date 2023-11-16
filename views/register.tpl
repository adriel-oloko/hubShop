{{meta}}
		
		<title>HUB || Sign Up</title>
{{header}}

			<br />
			<br />
			
			<div style="margin: auto; width: 100%; height: auto; ">
				<div style="width: 80%; height: auto; border: 0px solid #00182B; margin: auto; border-radius: 25px; box-shadow: 0px 0px 14px #00182B; background: #F3F0F0; ">
				
					<div style="width: 100%; height: auto; margin: auto; margin-bottom: 45px;">	
						<div style="margin: auto; border-radius: 50%; border: 1px solid #010070; width: 40px; height: 40px;position: relative; top: 15px; background: #fff; box-shadow: 0px 0px 10px #001895; padding: 13px;">
						<img src="./images/logo.png" style="width: 100%;height:auto;">
						<br />
					</div>
				</div>
				
				<hr />
				<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">Register</h4>
				<form action="/register" method="post" enctype="multipart/form-data">
				<div style="width: 80%; height: auto; margin: auto; ">
					<input name = "first_name" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="First name" required/>
					
					<input name = "last_name" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Last name" required/>
					
					<input name = "email" type="email" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Email" required/>
					
					<input name = "phone" type="phone" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Phone" required/>
					<input name="password" type="password" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Password" required/>
				
				<input type="submit" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px; outline: none; verical-align: middle;" value="Register" />
				
				<br />
			
			</form>
			<hr style="width: 70%;"/>
					<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">OR</h4>
						<a href="/login"><input type="button" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px; outline: none;" value="Login"/></a>						<br /><br />
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