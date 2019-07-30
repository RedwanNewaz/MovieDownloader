<?php

// class AsyncOperation extends Thread {

//     public function __construct($arg) {
//         $this->arg = $arg;
//     }

//     public function run() {
//         if ($this->arg) {
//             $sleep = mt_rand(1, 10);
//             printf('%s: %s  -start -sleeps %d' . "<br>", date("g:i:sa"), $this->arg, $sleep);
//             sleep($sleep);
//             printf('%s: %s  -finish' . "<br>", date("g:i:sa"), $this->arg);
//         }
//     }
// }




abstract class  program{
  private $executing;
  private $backend;
  protected $logFile;

  public function background()
  {
    // $this->backend = new AsyncOperation(4);
    // $this->backend->start();

  }

  public function exec()
  { 
    $this->executing = true;
    echo "start new download $this->executing<br>";
    $this->background();
    // sleep(10);
    // $this->backend->join();
    
  }

  public function print_json_file($data)
  {
    $jsonIterator = new RecursiveIteratorIterator(
    new RecursiveArrayIterator(json_decode($data, TRUE)),RecursiveIteratorIterator::SELF_FIRST);

    foreach ($jsonIterator as $key => $val) {
      if(!is_array($val)) {
          echo "$key :\t $val <br>";
      }
    }
  }

  public function json_reader($file)
  {
    error_reporting(E_ALL);
    $data = file_get_contents($file);
    $this->print_json_file($data);
    //return php array from json file 
    return (json_decode($data, true));
    
  }

  public function json_writer($file, $posts)
  {
      $fp = fopen($file, 'w');
      fwrite($fp, json_encode($posts));
      fclose($fp); 
  }



  public function sanity_check()
  {
    // check there exist a log file 
    $this->logFile = "log.json";

    if (file_exists($this->logFile)) {
      echo "The file $this->logFile exists <br>";
    } else {
        echo "The file $this->logFile does not exist <br>";
        return true;
    }
    //if there is a log file then read it 
    echo "reading  $this->logFile <br>";

    // read the flag complete 
    $data = $this->json_reader($this->logFile);

    return $data["0"]["status"]<2;

  }
}

class downloader extends program{

  public function log_writer($name, $url )
  {
    
    // append date to json file to track download time
      $date = date("D M d, Y G:i");
      $posts[] = array(
      'date'=>$date,
      'status'=>0,
      'file'=> $name, 'url'=> $url);

      // create a json file at current directory 
     
      $this->json_writer("log.json", $posts);
  }

  public function run()
  {
    echo "running downloader <br>";
    $this->exec();
  }

  public function finish()
  {
    $data = $this->json_reader($this->logFile);
    $data["0"]["status"] = 1;
    $this->json_writer("log.json", $data);

  }

}

?>