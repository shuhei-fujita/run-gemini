source .env
API_KEY=$API_KEY

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:streamGenerateContent?key=${API_KEY} \
        -H 'Content-Type: application/json' \
        --no-buffer \
        -d '{ "contents":[{"parts":[{"text": "Write long a story about a magic backpack."}]}]}' \
        2> /dev/null | grep "text"
