interactive_shell () {
    # docker exec -it $(docker ps -q -l --filter ancestor=mu-capstone-roommate-server-docker_core_api) /bin/bash
    
    docker exec -it $(docker ps -q -l) /bin/bash
}

interactive_shell
