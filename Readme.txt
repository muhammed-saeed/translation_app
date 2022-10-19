1- first install nodejs using conda
conda install -c conda-forge nodejs

2- load the json server file
json-server --watch .\data\db.json --port 8000

3- the ngrok

npx ngrok http 3000 --host-header="localhost:3000"