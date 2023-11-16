{{meta}}

		<title>HUB || Dashboard</title>
{{header}}

		<br />

		<center><h4>Dashboard</h4></center>
		<hr style="margin: auto; width: 80%;"/>

		<div id="main">
		<br>
		<input type="text" id="myInput" onkeyup="srch()" placeholder= "Search by Name...." title="Type in a name" >

		<table id="myTable">
			<tr class="header">
				<th style="width:5%;">ID</th>
				<th style="width:28%;"><center>Title</center></th>
				<th style="width:20%; "><center>Data</center></th>
				<th style="width:28%; "><center>Price</center></th>
				<th style="width:10%; "><center><i class="fa fa-cog fa-lg" style="margin-left: 5px;"></i></center></th>
			</tr>

			{% for entry in all %}
			<tr>
				<td>{{entry[0]}}</td>
				<td><center>{{entry[1]}}</center></td>
				<td id ="chk"><center>{{entry[2]}} {{entry[3]}}, {{entry[4]}}</center></td>
				<td id ="chk"><center>{{entry[5]}}</center></td>

				<td style="color: blue;">				<a href="/delete-post/{{entry[0]}}"><center><i class="fa fa-trash" style="margin-left: 0px; color: red;"></i></center></a></td>
			</tr>
			{% endfor %}

		</table>
		</div>
		<br />



		<br />		<br />		<script>
		function srch() { var input, filter, table, tr, td, i; input=document.getElementById("myInput"); filter=input.value.toUpperCase(); table=document.getElementById("myTable"); tr=table.getElementsByTagName("tr"); for (i = 0; i < tr.length; i++) { td = tr[i].getElementsByTagName("td")[1]; if (td) { if (td.innerHTML.toUpperCase() .indexOf(filter) > -1) { tr[i].style.display = ""; } else { tr[i].style.display = "none"; } } } } </script>

	</body>
</html>