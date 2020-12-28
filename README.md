# Usage

* To build the image:
  
`docker build . -t res-stix-shifter`

* To run the container:

`docker run -d --rm -e API_KEY=<RESILIENT_API_KEY> -e API_PASSWORD=<RESILIENT_API_PASSWORD> -e ORG_ID=<ORG_ID> -e HOST=<RESILIENT_HOST> -p 5000:5000 res-stix-shifter`

* To run the query

` curl -H "Content-Type: application/json" --data @query.json  http://localhost:5000/rest/query_artifacts`

where the json data `query.json` file looks like

`{
"query":"[domain-name:value = 'ibm.com']"
}
`



