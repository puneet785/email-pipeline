pipeline { 
   agent {label 'osd_machine'}

   stages{ 
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
       stage('Run python'){
           steps{
            script{
               def command= "python3 ${env.workspace}/agile.py"
               def process = command.execute()
               process.waitFor()
            }
           }
       }
   
   }


}
