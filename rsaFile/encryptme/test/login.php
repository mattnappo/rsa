<html lang="en">
	<head>
		<link rel="icon" type="image/ico" href="">
		<link rel="stylesheet" type="text/css" href="w3.css">
		<title>Login</title>
	</head>
		<div id="correct" class="w3-modal">
			<div class="w3-modal-content">
				<div class="w3-container">
		    	<span onclick="document.getElementById('correct').style.display='none'" class="w3-button w3-display-topright">&times;</span>
		      		<p>Correct credentials.</p>
		    	</div>
		  	</div>
		</div>
		<div id="wrong" class="w3-modal">
			<div class="w3-modal-content">
				<div class="w3-container">
		    	<span onclick="document.getElementById('wrong').style.display='none'" class="w3-button w3-display-topright">&times;</span>
		      		<p>Unknown credentials.</p>
		    	</div>
		  	</div>
		</div>
		<div id="user" class="w3-modal">
			<div class="w3-modal-content">
				<div class="w3-container">
		    	<span onclick="document.getElementById('user').style.display='none'" class="w3-button w3-display-topright">&times;</span>
		      		<p>Cannot leave username blank.</p>
		    	</div>
		  	</div>
		</div>
		<div id="pass" class="w3-modal">
			<div class="w3-modal-content">
				<div class="w3-container">
		    	<span onclick="document.getElementById('pass').style.display='none'" class="w3-button w3-display-topright">&times;</span>
		      		<p>Cannot leavy password blank.</p>
		    	</div>
		  	</div>
		</div>
		<div class="w3-row w3-padding-large">
			<form class="w3-container w3-third" method="post" action="login.php">
				<h1 class="w3-center">Login</h1>
				<label>Username</label>
				<input class="w3-input w3-hover-border-red" name="username" type="text">
				<label>Password</label>
				<input class="w3-input w3-hover-border-red" name="password" type="password">
				<button class="w3-button w3-margin-top w3-red w3-right" name="login" onclick="document.getElementById('success').style.display='block'">Login</button>
			</form>
		</div>
	</body>
</html>
<?php
	//server stuff
	$servername = "localhost";
	$serverUser = "root";
	$dbName = "access";
	$serverPass = "";
	//form stuff
	$username = "";
	$password = "";
	$secPass = "";
	
	if(isset($_POST['login'])) {
		if($username!="") {
			if($password!="") {
				$username = $_POST['username'];
				$password = $_POST['password'];

				//Connect to database and test connection
				$secPass = md5($password);
				$conn = new mysqli($servername, $serverUser, $serverPass, $dbName);
				if ($conn->connect_error) {
				    die("Connection failed: " . $conn->connect_error);
				}

				//make sql stuff
				$sql = "SELECT id, username, password FROM users";
				$result = $conn->query($sql);
				if ($result->num_rows > 0) {
				    // output data of each row
				    while($row = $result->fetch_assoc()) {
				        if($row['username'] == $username && $row['password'] == $secPass) {
				        	echo '<script>document.getElementById("correct").style.display="block";</script>';
				        	$username = "";
							$password = "";
							$secPass = "";
				        } else {
				        	echo '<script>document.getElementById("wrong").style.display="block";</script>';
				        	$username = "";
							$password = "";
							$secPass = "";
				        }
				    }
				} else {
				    echo "<script>alert('Error: Database Empty');</script>";
				}
			} else {
				echo '<script>document.getElementById("pass").style.display="block";</script>';
				$username = "";
				$password = "";
				$secPass = "";
			}
		} else {
			echo '<script>document.getElementById("user").'\style.display="block";</script>';
		    $username = "";
			$password = "";
			$secPass = "";
		}

	}
?>