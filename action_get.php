
<!-- Download button -->
<style type="text/css">
    input#search
    {
      padding: 16px 32px;
      font-size: 16px;
      margin: 4px 2px;
      background-color: #008CBA;
      color: white;
    }
</style>



<html>
  <!-- Mobile friendly -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

  <body>
  <font color="red"> Movie name: </font><?php echo $_GET["file"]; ?><br>
  <font color="blue">Downloading from: </font><?php echo $_GET["link"]; ?> <br><br>
  
  
  <?php
    include("launcher.php");
    $download = new downloader;
    $name= $_GET["file"];;
    $url= $_GET["link"];
    if($download->sanity_check())
    {
      $download->log_writer($name, $url);
      $download->run();
    }
    else{
      echo "cannot download \n";
      
    }
  ?>                                                    

    <form action="process.py">
      <input type="submit" value="Confirm" id="search" class="search"><br>
    </form>

  </body>

</html>
