localBuild () {
    #docker-compose up -d
    docker-compose up --build
    
    echo ""
    echo "When you're satisfied, commit these changes, then run:"
    echo "./scripts/push_image.sh"
}

localBuild
