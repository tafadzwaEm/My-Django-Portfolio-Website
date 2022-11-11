<?php


if($_POST["message"]) {


mail("mukomberoemmanuel@gmail.com", ["subject"],


$_POST["message"]. ["email"]);


}


?>