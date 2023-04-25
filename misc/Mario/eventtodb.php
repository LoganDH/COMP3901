<?php
	$casename = $_POST['casename'];
	$createddate = $_POST['createddate'];
	$logevent = $_POST['logevent'];
	$location = $_POST['location'];


	// Database connection
	$conn = new mysqli('localhost','root','','capstone');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die(" Failed to send : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("insert into feedback(casename, createddate, logevent, location) values(?, ?, ?, ?)");
		$stmt->bind_param("ssss", $casename, $createddate, $logevent, $location);
		$stmt->execute();
		
		echo "Report has been saved successfully!...";
		$stmt->close();
		$conn->close();
	}
?>