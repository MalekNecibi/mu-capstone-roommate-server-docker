pushImage () {
   
   # rebuild (by running)
   docker-compose up --build --detach
   # stop
   docker-compose down
   # tag
   docker tag mu-capstone-roommate-server-docker_core_api:latest 618832047066.dkr.ecr.us-east-1.amazonaws.com/bunkiez_server_docker:latest
    # authenticate
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 618832047066.dkr.ecr.us-east-1.amazonaws.com
   # push
   docker push 618832047066.dkr.ecr.us-east-1.amazonaws.com/bunkiez_server_docker:latest
   
   echo ""
   echo "Make sure you're also commiting these changes!"
}

pushImage

