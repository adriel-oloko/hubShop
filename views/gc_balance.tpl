{{meta}}
		
		<title>HUB || Gift card balance</title>
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
				<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">Gift Card Balance</h4>
				
				<div style="width: 80%; height: auto; margin: auto; ">
					<input id = "code" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Code" required/>
					
					<input id = "pin" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" placeholder="Pin" required/>
				
				<button type="submit" id="gc_button" onClick="CheckGC()" type="submit" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px; outline: none; verical-align: middle; background: #ccc;" value="Next">Next</button>
				
			
			<input id="gc_balance" type="text" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%; display: none;" disabled/>
			
			<br />
			
			<script>
			
			function GCgood() {
		document.getElementById("gc_button").style.display="none";
		document.getElementById("gc_balance").style.display="";
		}
	
	
	var httpRequest = new XMLHttpRequest();
	
	function CheckGC() {
		
		var code = document.getElementById("code").value;
		var pin = document.getElementById("pin").value;
		GCgood();
		httpRequest.onreadystatechange = writeContent;
		
		httpRequest.open('POST', '/giftcard/balance');
		httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	
		httpRequest.send("code="+code+"&pin="+pin);
		
		function writeContent() {
			if(httpRequest.readyState === 4) {
				if(httpRequest.status == 200) {
				var response = httpRequest.responseText;
					document.getElementById("gc_balance").value = "Balance: ₦"+response;
					GCgood();
				}
				else {
					document.getElementById("gc_balance").value = "Error encountered!!";
					GCgood();
				}
			}
			else {
				// response not ready yet
			}
		}
	}
	
	
</script>
			
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