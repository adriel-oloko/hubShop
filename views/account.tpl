{{meta}}
		
		<title>HUB || Account</title>
{{header}}
 		
		<br />
		
		<center><h4>Account activity</h4></center>
		<hr style="margin: auto; width: 80%;"/>
		
		<div id="main">
		<br>
		<input type="text" id="myInput" onkeyup="srch()" placeholder= "Search by Name...." title="Type in a name" >
		
		<table id="myTable">
			<tr class="header">
				<th style="width:5%;">ID</th>
				<th style="width:20%;"><center>Date</center></th>
				<th style="width:28%; "><center>Payment</center></th>
				<th style="width:28%; "><center>Status</center></th>
				<th style="width:10%; "><center><i class="fa fa-cog fa-lg" style="margin-left: 5px;"></i></center></th>
			</tr>
			
			{% for entry in tr_hist %}
			<tr>
				<td>{{entry[0]}}</td>	
				<td><center>{{entry[4]}} {{entry[5]}}, {{entry[6]}}</center></td>
				<td id ="chk"><center>{{entry[8]}}</center></td>	
				
				{% if entry[7] == "O" %}
				<td style="font-size: 15px; color: blue;"><center><i class="fa fa-shopping-basket"></i></center></td>									
				{% endif %}
				
				{% if entry[7] == "T" %}
				<td style="font-size: 15px; color: blue;"><center><i class="fa fa-truck"></i></center></td>						
				{% endif %}
				
				{% if entry[7] == "D" %}
				<td style="font-size: 15px; color: blue;"><center><i class="fa fa-download"></i></center></td>									
				{% endif %}
				
				<td style="color: blue;">				<a href="/transaction/tracking/{{entry[0]}}"><center><i class="fa fa-envelope" style="margin-left: 0px; color: blue;"></i></center></a></td>
			</tr>
			{% endfor %}
			
		</table>
		</div>
		<br />
		
		

		<br />		<br />		<script>
		function srch() { var input, filter, table, tr, td, i; input=document.getElementById("myInput"); filter=input.value.toUpperCase(); table=document.getElementById("myTable"); tr=table.getElementsByTagName("tr"); for (i = 0; i < tr.length; i++) { td = tr[i].getElementsByTagName("td")[1]; if (td) { if (td.innerHTML.toUpperCase() .indexOf(filter) > -1) { tr[i].style.display = ""; } else { tr[i].style.display = "none"; } } } } </script>

	</body>
</html>