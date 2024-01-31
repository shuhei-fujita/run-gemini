source .env
API_KEY=$API_KEY

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{
          "text": "What is the meaning of life? Response is 160 characters."}]}]}' 2> /dev/null
