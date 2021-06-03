
# odh-smaland

This repo contains the code for a key-value store used within the ODH project, which can be used to server global parameters. These parameters a created at deploy time (so it is a read-only kv store).

# Using the function
    curl \
      --silent \
      --request GET \
      --header "Content-Type: application/json" \
      --header "Authorization: bearer ${identity_token}" \
      https://europe-west1-"${CONFIG_PROJECT}".cloudfunctions.net/"${CONFIG_PROJECT}"-kvstore/kv/[MY_KEY]")


# getting a identity token in a cloud builder
Check below the code sample to get a identity token with a cloudbuilder

 

      AUDIENCE="https://europe-west1-${CONFIG_PROJECT}.cloudfunctions.net/${CONFIG_PROJECT}-kvstore"
      SERVICE_ACCOUNT="kvstore@${CONFIG_PROJECT}.iam.gserviceaccount.com"
    
      token=$(curl \
        --silent \
        --request POST \
        --header "content-type: application/json" \
        --header "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data "{\"audience\": \"${AUDIENCE}\" }" \
	    "https"://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/${SERVICE_ACCOUNT}:generateIdToken")
    
       
      identity_token=$(echo "${token}" | python3 -c "import sys, json; j=json.loads(sys.stdin.read()); print(j['token'])")


