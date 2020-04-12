<html>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>    
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script data-main="scripts/main" src="https://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
    <script src="main.js"></script>

    <body>
        <div class="container">
            <p class="text-primary" id="txt"></p></br>
            <p class="text-primary" id="fromPHP"></p></br>
            <p class="text-success" id="answer-yes"></p>
            <p class="text-danger" id="answer-no"></p>
        </div>
        <?php            
            $tid=$_POST['txt1'];
            $f_temp=$_FILES["file1"]["tmp_name"];
            $f_name=$_FILES["file1"]["name"];
            move_uploaded_file($f_temp,"uploads/".$f_name);            
            $out = shell_exec("python python/demo1.py $f_name");
            $final=chop($out);            

        ?>
    </body>
    <script>
        web3=new Web3(web3.currentProvider);
        eth = web3.eth;
        let data;
        async function getAccount() {
            const td="<?php echo $tid;?>";
            ethereum.enable();
            eth.getTransaction(td).then(
                function(result){                      
                        data=result.input 
                        console.log(data);                                                                    
                }
            );                      
        }
        function compare(){
            if(typeof data != undefined){
                var s=data.substring(2);
                document.getElementById('fromPHP').innerHTML="Your File's Hash - "+" <?php echo $final ?>";
                document.getElementById('txt').innerHTML="Stored Hash from Blockchain - "+s;            
                if(s==="<?php echo $final ?>"){
                    document.getElementById('answer-yes').innerHTML="Validated Successfully! The record is original.";
                }
                else{
                    document.getElementById('answer-no').innerHTML="Oh!! Record doesn't seems to be original.";
                }
            }            
        }
        getAccount()
        setTimeout(compare, 2000);    
    </script>
</html>