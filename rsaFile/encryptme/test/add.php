<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "access";
	$webuser = "matt";
	$webpass = "aaron";
	

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}
	$sql = "INSERT INTO users (username, password) VALUES ('$webuser', '$webpass');";

	if ($conn->query($sql) === TRUE) {
	    echo "New record created successfully";
	} else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	}

	$conn->close();
?>