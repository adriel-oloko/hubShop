{{meta}}

		<title>HUB || Tracking Order {{track[0]}}</title>
{{header}}

			<br />
			<br />


			<hr />

		<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600;">Your order, #{{track[0]}}</p>

		<div style="width: 90%; border: 1px solid #00182B; border-radius: 5px; height: auto; padding: 10px; margin: auto;">

			<div style="width: 100%; float: right; margin-bottom: 30px;">
				<div style="width: 40%; float: right; margin-left: 10px; border: 1px solid red; height: auto;">

					<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 10px;">#{{track[0]}}</p>
					<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 10px;">{{name[0]}} {{name[1]}},</p>
					<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 10px;">{{address[0]}}, {{address[1]}}, {{address[2]}}, {{address[3]}}.</p>
					<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 10px;">{{track[4]}} {{track[5]}}, {{track[6]}}</p>

				</div>
			</div>

			<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 10px;">Order ID: #{{track[0]}},</p>

			<h4 style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600;">Content</h4>
			<hr>

			{%for log in trh%}
			<li style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 10px;">{{log[4]}} - {{log[5]}} (×{{log[6]}})</li>
			<br />
			{%endfor%}

			<hr style="width: 30%; float: left; padding-left: 10px;" />
			<br />
			<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 13px;">Total: ₦{{price}}</p>

			<hr />

			<!--
			{%if track[7] == "O"%}
			<div style="width: 75%; margin: auto; border: 1px solid green;">

			<table style="width: 100%; text-align: center;">
				<tr>
						<td class="sponsor">	<i class="fa fa-shopping-basket" ></i></td>
					<td class="sponsor"><i class="fa fa-truck"></i></td>
					<td class="sponsor"><i class="fa fa-download"></i></td>
				</tr>

			</table>

			<section style="width: 19%; background-color: green; float; right; height: 10px;"></section>
			</div>

			{%endif%}


			{%if track[7] == "T"%}
			<div style="width: 75%; margin: auto; border: 1px solid green;">

			<table style="width: 100%; text-align: center;">
				<tr>
						<td class="sponsor">	<i class="fa fa-shopping-basket" ></i></td>
					<td class="sponsor"><i class="fa fa-truck"></i></td>
					<td class="sponsor"><i class="fa fa-download"></i></td>
				</tr>

			</table>

			<section style="width: 53%; background-color: green; float; right; height: 10px;"></section>
			</div>

			{%endif%}


			{%if track[7] == "D"%}
			<div style="width: 75%; margin: auto; border: 1px solid green;">

			<table style="width: 100%; text-align: center;">
				<tr>
						<td class="sponsor">	<i class="fa fa-shopping-basket" ></i></td>
					<td class="sponsor"><i class="fa fa-truck"></i></td>
					<td class="sponsor"><i class="fa fa-download"></i></td>
				</tr>

			</table>

			<section style="width: 100%; background-color: green; float; right; height: 10px;"></section>
			</div>

			{%endif%}
			-->
			<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 13px;">Your order (of id #{{track[0]}}) was placed successfully, and is currently pending confirmation before being put in transit to be delivered to you.</p>
			<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 13px;">Order confirmations usually takes less than 24 hours to be completed. In case of any questions, do reach out to us via any of our online 24/7 available customer care platforms.</p>


			<br />
			<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 13px; line-height: 0px;">Cheers, </p>

			<p style="padding-left: 30px; font-family: 'Nunito', sans-serif; font-weight: 600; font-size: 13px;">HUB Team.</p>

		</div>



			<br />
			<br />

		<div id="footer">
			<hr />

			<h3 style="margin-bottom: -9px;">Contact Us</h3>
			<br />
			<p style="padding:0px 20px 0px 20px;text-align: center;">services.hubshop@gmail.com<br /><br />No 1, Ologolo village road, Jakande close, Lekki peninsula, Lagos, Nigeria<br /></p>

			<br />

			<table style="border: None; width: 30%; margin: auto; font-size: 19px;">
				<tr>
					<th><i class="fa fa-facebook"></i></th>
					<th><i class="fa fa-instagram"></i></th>
					<th><i class="fa fa-twitter"></i></th>
					<th><i class="fa fa-linkedin"></i></th>
				</tr>
			</table>

			<hr style="width: 70%; text-align: center;" />
			<br />
			<p>Hub Technologies<p>
			<p>©{{yr}}</p>
			<br />
		</div>


		<script>
var slideIndex = [1,1];
var slideId = ["mySlides1", "mySlides2"]
showSlides(1, 0);
showSlides(1, 1);

function plusSlides(n, no) {
  showSlides(slideIndex[no] += n, no);
}

function showSlides(n, no) {
  var i;
  var x = document.getElementsByClassName(slideId[no]);
  if (n > x.length) {slideIndex[no] = 1}
  if (n < 1) {slideIndex[no] = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex[no]-1].style.display = "block";
}
</script>
	</body>
</html>