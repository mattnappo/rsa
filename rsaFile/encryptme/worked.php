<?php
	session_start();
	if(isset($_SESSION['id'])) {
		echo "welcome";
	} else {
		header("location: login.php");
	}
	session_unset($_SESSION['id']);

?>