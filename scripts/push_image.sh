# IMPORTANT: Run this from the root of the repository (./scripts/push_image.sh)
pushImage () {
   
    local image_name="mu-capstone-roommate-server-docker_core_api"
    
    # stop existing instance(s)
    # docker rm $(docker stop $(docker ps -a -q --filter ancestor=$image_name))
    docker stop $(docker ps -a -q  --filter ancestor=$image_name)
    
    # rebuild the image
    docker build -t $image_name .
    
    # Run it to test it works (optional)
    #container_id=$(docker run -dp 8200:15400 $image_name)
    #docker stop $container_id

    # tag for release
    docker tag mu-capstone-roommate-server-docker_core_api:latest 618832047066.dkr.ecr.us-east-1.amazonaws.com/bunkiez_server_docker:latest
    

    # authenticate with image repository 
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 618832047066.dkr.ecr.us-east-1.amazonaws.com
    
    # Push up new image!!
    docker push 618832047066.dkr.ecr.us-east-1.amazonaws.com/bunkiez_server_docker:latest
   
    echo ""
    echo "Make sure you're also commiting these changes!"
}

pushImage

