<?php  
	session_start();
	header('location:login.html');
	
	$conn=mysqli_connect('localhost','root','');
	mysqli_select_db($conn,'myfirstdb2');
	$emailf=$_POST['email'];
	$passf=$_POST['password'];
	$usernamef=$_POST['username'];
	$email=test($emailf);
	$pass=test($passf);
	$username=test($usernamef);
	$s="select * from firsttable where email='$email' || username='$username'";
	$result=mysqli_query($conn,$s);
	$num=mysqli_num_rows($result);
	if($num==1){
		echo "Username or email is already taken";
	}
	else{
		$reg="insert into firsttable(email,password,username) values('$email','$pass','$username')";
		mysqli_query($conn,$reg);
		echo "Registration Success";
	}
	function test($da)
	{
		$da=trim($da);
		$da=stripslashes($da);
		$da=htmlspecialchars($da);
		return $da;
	}
?>
