{{meta}}

		<title>HUB || Search - {{query}}...</title>
{{header}}

		<center><h3>Search</h3></center>
		<div style="width: 90%; margin: auto;">
		{% if cnt[0] <= 1 %}
		<h3>{{cnt[0]}} result for {{query}}</h3>
		{% endif %}

		{% if cnt[0] > 1 %}
		<h3>{{cnt[0]}} results for {{query}}</h3>
		{% endif %}
		</div>

		<hr style="margin: auto; width: 80%;"/>

		<br />


		<div id="main">
 			<div class="post">

 				{% for post in posts %}
				<div style="width: 100%; border: 0px solid #aaa; height: 125px; padding: 0px;">
					<div style=" width: 30%; float: left; height: 85%;">					<img src="/post/images/{{post[9]}}" style="padding-bottom: 5px; height: 100%; border: 0px solid #aaa;"/></div>
					<div style=" width: 69%; float: right; height: 110px;">
						<b><p style="padding-left: 10px; font-family: 'Nunito', sans-serif; text-align: left;">{{post[1]}} - {{post[8]}}</p></b>
						<b><p style="padding-left: 10px; font-family: 'Nunito', sans-serif; text-align: left;">₦{{post[2]}}</p></b>
					</div>
					<div style="width: 48%; height: auto; float: left;">
						<a href="/pr/{{post[0]}}/{{post[1]}}"><button style="border:1px solid black; width: 100%; height:auto; background-color:white;">Preview</button></a>
					</div>

					<div style="width: 48%; height: auto; float: right;">				<form action="/add-cart/{{post[0]}}" method="post" enctype="multipart/form-data">				 <button style="float: right;border:1px solid black; width: 100%; height:100%; background-color:white;">Cart</button> <input name="quantity" id = "quantity" style="display:none;" value="1"/>			 </form>			</div>
			</div>
			<br />
			<hr>

			{% endfor %}
		</div>
	</div>



		<table style="width: 90%; margin: auto; border: 0px solid red;">
			<tr>
				{% if page > 0 %}
					{% if page == 1 %}
						<th><a href="/query/{{query}}"><button style="padding: 5px; border: 1px solid grey; float: left; border-radius: 5px;">Next</button></a></th>
					{% else %}
						<th><a href="/query/{{query}}/{{page-1}}"><button style="padding: 5px; border: 1px solid grey; float: left; border-radius: 5px;">Next</button></a></th>
					{% endif %}
				{% endif %}

				{% if has_next %}
					<th><a href="/query/{{query}}/{{page+1}}"><button style="padding: 5px; border: 1px solid grey; float: right; border-radius: 5px;">Previous</button></a></th>
				{% endif %}
			</tr>
		</table>


		<br /><br />

		{{footer}}
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