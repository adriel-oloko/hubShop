{{meta}}

		<title>HUB || Upload</title>
{{header}}


		<br />

		<center><h3>Upload</h3></center>
		<hr style="margin: auto; width: 80%;"/>

		<br />

		<div id="main" style="text-align: left;">

 			<div class="post">

				<form action="/upload" method="post" enctype="multipart/form-data">
		<div style="width:99%;">
			<input style="color: black; background-color:white; border:1px solid white; border-bottom: 1px solid gold; width:70%; height: auto" id="title" name="title" placeholder="Title" value="{{all[2]}}" />


		</div>

<br>
<br>

<script src="https://cdn.tiny.cloud/1/hl4pp34o5nonsppphyg5bd5r5t78za90axbzrk9wj5wgtwld/tinymce/5/tinymce.min.js" referrerpolicy="origin"></script>

<div style="height: auto; width: 100%; box-shadow: 5px 6px 12px #aaa;background: black; border-radius:5px; padding: 12px 0px 12px 0px;">


<textarea name="txt_save" id="myTextarea"></textarea>
</div>

<script type="text/javascript">
tinymce.init({
  selector: '#myTextarea',  // change this value according to your HTML
  /*content_style = "body { background: red;font-family: 'Nunito', sans-serif;}",*/

  content_css: ["/css/rjt.css",
    "https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap",
  ],
  height: 500,
  plugins: [
      'advlist autolink autosave lists link charmap print preview hr anchor pagebreak',
      'searchreplace wordcount visualblocks visualchars code fullscreen',
      'insertdatetime nonbreaking save table contextmenu directionality',
      'emoticons template paste textcolor colorpicker textpattern'
    ],

  toolbar1: 'undo redo | styleselect | bold italic fontsizeselect | alignleft aligncenter alignright alignjustify ',
  toolbar2: 'bullist numlist outdent indent | forecolor backcolor emoticons',
    toolbar3: 'save print preview link',
    image_advtab: true
});


</script>

<br>
<br>

<div style="background-color:lightgrey; padding:4px; border-left:0px solid lightgrey; height: auto; border: 1px solid lightgrey; border-radius: 5px;">

	<input style="color: black; background-color:lightgrey; border:1px solid lightgrey; border-bottom: 1px solid gold; width:70%; height: auto; margin-bottom: 5px;" name="brand" placeholder="Brand" value="{{all[1]}}" />
	<br />
	<input style="color: black; background-color:lightgrey; border:1px solid lightgrey; border-bottom: 1px solid gold; width:70%; height: auto; margin-bottom: 5px;" name="price" placeholder="Price" value="{{all[1]}}" />


	<input type="file" name="img1"/>

<textarea style="margin-top: 5px; border: 1px solid gold; border-radius: 5px; height: 75px; width: 95%;" name="features" placeholder="Features"></textarea>
<br />
	<textarea style="margin-top: 5px; border: 1px solid gold; border-radius: 5px; height: 75px; width: 95%;" name="tags" placeholder="Tags seperated by spaces...">{{tag}}</textarea>

</div>

<br>

<input type="submit" style="bottom: 15px; float: right; background-color: gold; height: 30px; width: 25%; margin-right: 25px; border: 1px solid gold; border-radius: 5px;" placeholder="Submit" ></input>

			</div>
		</div>



		<br /><br />

		{{footer}}
	</body>
</html>