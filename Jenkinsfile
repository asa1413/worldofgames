node()
{

    try

        {
         stage("image")
          {
             dir('C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames'){
            bat 'docker build . -t asa1413/worldofgames:latest'
           }
          }
        stage("build")
        {
           dir('C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames'){
            bat 'docker-compose up -d'
           }
        }
        stage("test")
        {
          dir('C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames'){
              bat (script: 'python e2e.py')
          }
        }
         stage("stop")
        {
           dir('C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames'){
            bat 'docker-compose down'
           }
        }


        stage("push")
        {
           dir('C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames'){
            bat 'docker-compose push'
           }
        }

        }
    catch (err) {
        stage("stop_in fail")
        {
           dir('C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames'){
            bat 'docker-compose down'
           }
        }
    }
}
