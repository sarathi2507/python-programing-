<?php
	session_start();
	if(!isset($_SESSION['email'])){
		header('location:login.html');
	}
?>

<!DOCTYPE html>
<html>
<head>
	<title>Your Account</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
	<div class="container">
		<a class="float-right so" href="logout.php"> LOGOUT </a>
		<h1 class="mo">Welcome <?php echo $_SESSION['email'];?></h1>
	</div>

</body>
</html>