localBuild () {
    local image_name="mu-capstone-roommate-server-docker_core_api"
    
    # docker rm $(docker stop $(docker ps -a -q  --filter ancestor=mu-cap^Cone-roommate-server-docker_core_api))
    docker stop $(docker ps -a -q  --filter ancestor=$image_name)
    
    docker build -t $image_name .
    
    docker run -dp 8200:15400 $image_name

    echo ""
    echo "When you're satisfied, commit these changes, then run:"
    echo "./scripts/push_image.sh"
}

localBuild
