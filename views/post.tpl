{{meta}}

<title>HUB || {{data[1]}} - {{data[8]}}</title>
{{header}}

 	<div class="post" style="box-shadow: 5px 6px 12px #aaa; width: 90%; margin: auto; padding: 5px;">
		<div class="slideshow-container">

			{%for image in images %}
			<div class="mySlides1">
				<img src="/post/images/{{image[0]}}" />
			</div>
			{% endfor %}

<a class="prev" onclick="plusSlides(-1, 0)">&#10094;</a> <a class="next" onclick="plusSlides(1, 0)">&#10095;</a></div>


<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 700;">{{data[1]}} - {{data[8]}}</p><p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-weight: 600;">₦ {{price}}</p>
<p style="padding-left: 10px; font-family: 'Nunito', sans-serif; font-size: 13px; font-weight: 600;">Brand| <a>{{data[3]}}</a></p>


<div style="padding: 5px; border: 1px solid #ccc; height: 40px; width: 90%; margin: auto; font-size: 14px; border-radius: 15px;">

				<input name="quantity" id="quantity" type="text" style="text-align: center; border: 1px solid #ccc; width: 11%; float: left; font-size: 16px; height: 28px; outline: none; border-radius: 15px; padding: 5px;" placeholder="Qty" />
				<button onclick="add_cart()" style="width: 84%; float: right;border: 1px solid #ccc; border-radius: 15px; height: 40px; font-size: 16px; background: gold;">Add to cart <i id="icon-cart" class="fa fa-shopping-cart"></i> <i style="display: none;" id="icon-check" class="fa fa-check"></i><i style="display: none;" id="icon-cross" class="fa fa-close"></i></button>
			<script>
				var httpRequest = new XMLHttpRequest();

			function add_cart() {
				httpRequest.onreadystatechange = writeContent;
				var quantity = document.getElementById("quantity").value;
				httpRequest.open('POST', '/add-cart/{{id}}');

				httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

				httpRequest.send("quantity="+quantity);

				function writeContent() {
					if(httpRequest.readyState === 4) {
						if(httpRequest.status == 200) {
							var response = httpRequest.responseText;
        icon_switch()

       }
       else {
        icon_switch_fail();
        alert("Error adding item to cart!")
       }
      }
      else {
       // response not ready yet
      }
     }
    }

				function icon_switch() {
					document.getElementById("icon-cart").style.display="none";
					document.getElementById("icon-cross").style.display="none";
					document.getElementById("icon-check").style.display="";
				}

				function icon_switch_fail() {
					document.getElementById("icon-cart").style.display="none";
					document.getElementById("icon-check").style.display="none";
					document.getElementById("icon-cross").style.display="";
				}
			</script>
			</div>


<br />
<hr />


<div class="post">
	<h3 style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 15px;">Description</h3>
	<hr />
	<div style="font-size: 12px;"><p style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 12px;">{{xx}}</p></div>
</div>

<br /><br />

<div class="post">	<h1 style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 15px; line-height: 0px; margin-bottom: 0px;">Rating</h1>	<h3 style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 15px; line-height: 0px; margin-bottom: -10px;">4/5</h3>	<h3 style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 15px; color: gold;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star-o"></i></h3>	<hr />
	<h1 style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 15px; line-height: 0px; margin-bottom: 0px;">Review</h1>	<br>

	{% if no_comment %}
		<p style="padding: 3px; font-family: 'Nunito', sans-serif; font-size: 15px; text-align: center;">No review yet</p>
	{% else %}
	 {% for c in comments %}
	 <p style="line-height: 1.2; font-size: 15px;">{{c[3]}}</p>
	 	<p style="line-height: 0.5; font-size: 80%;">By <i><b>{{c[2]}}</b></i></p>
			<pre><i class="fa fa-clock-o" style="text-align:left;color:lightgrey;font-size:10px;"> {{c[6]}} {{c[7]}}, {{c[8]}} {{c[4]}}:{{c[5]}}</i></pre>
			<hr />
		{% endfor %}
	{% endif %}


<form action="/pr/{{id}}/{{data[1]}}" method="post" enctype="multipart/form-data">
	<textarea name="p_id" style="visibility: hidden;">3</textarea>
	<textarea name="author" type="text" style="margin-bottom:6px; border-radius:.5em;height:1.5em;float:left;" placeholder="Name"></textarea>
	<textarea name="comment" type="textarea" style="border-radius:.5em; height: 5em; width: 90%;" placeholder="Review..."></textarea>
	<br />
	<input value="Submit" type="submit" style="background-color:gold;border-radius:.5em;margin-top: 5px;height: 2em; border: 1px solid #ccc;" />
</form>
</div>

			</div>
<br />
<br />

{{footer}}
<p>©{{yr}}</p>
			<br />
		</div>
	</body>
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
</html>