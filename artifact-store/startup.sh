#!/bin/sh

###
# Starts a node application
###

# Exit if error
set -e

# This will execute a node application depending on NODE_ENV
# @input - none
# @output - none
main() {
    echo "Running in the $NODE_ENV environment."

    if [[ "$NODE_ENV" == "production" ]]; then
        node ./index.js
    elif [[ "$NODE_ENV" == "staging" ]]; then
        node ./index.js
    elif [[ "$NODE_ENV" == "development" ]]; then
        nodemon -L --watch "./" ./index.js
    else
        echo "Unknown environment, $NODE_ENV. Set NODE_ENV to (production, staging, development). Exiting build."
        exit 1
    fi
}

# This is a cleanup function.
# @input - none
# @output - none
cleanup_before_exit() {
    # This in intentionally left empty
    echo ""
}

# # Cleanup when exiting
trap cleanup_before_exit EXIT INT TERM

# Run the main process
main "$@"
