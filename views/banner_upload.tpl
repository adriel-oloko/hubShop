{{meta}}

		<title>HUB || Banner Upload</title>
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
				<h4 style="font-family: 'Nunito', sans-serif ; text-align: center;">Image Upload</h4>

				<div style="width: 80%; height: auto; margin: auto; ">
				<form action="/banner/upload" method="post" enctype="multipart/form-data">

					<input name = "img1" type="file" style="width: 94%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 20px;outline: none; padding-left: 5%;" required/>

				<button type="submit" id="gc_button" type="submit" style="width: 100%; height: 30px; border: 1px solid white; border-radius: 20px; margin: auto; margin-bottom: 10px; outline: none; verical-align: middle; background: #ccc;" value="Next">Next</button>


			</form>

			<br />


			</div>
		</div>
	</div>

		<br />
	<br />
	<div style="margin: auto; width: 100%; height: auto; ">
				<div style="width: 80%; height: auto; border: 0px solid #00182B; margin: auto; border-radius: 25px; box-shadow: 0px 0px 14px #00182B; background: #F3F0F0; ">

			<table style="width: 90%; margin: auto; padding: 5px; font-family: 'Nunito', sans-serif ;">
			{% for i in ix %}
				<tr>
					<th style="border-bottom: 1px solid #000;">{{i[0]}}</th>
					<th style="border-bottom: 1px solid #000;"><img src="/images/{{i[1]}}" style=" width: 70%; height: auto;" /></th>

					<th style="border-bottom: 1px solid #000;"><a href="/banner/delete/{{i[0]}}"><i class="fa fa-trash"></i></a></th>
				</tr>
			{% endfor %}

			</table>
		</div>
	</div>

		<br /><br />
{{footer}}
<p>©{{yr}}</p>
			<br />
		</div>
	</body>
</html>