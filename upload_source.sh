python3 creates3bucket.py

mkdir infrastructure/dbbuild

echo "zipfile for function"

cd api-server/source
zip -r ../../infrastructure/dbbuild/api-server.zip .
cd ../..

cd requests_layer
pip3 install -r requirements.txt --target python/lib/python3.9/site-packages
zip -r ../infrastructure/dbbuild/requests_layer.zip .
cd ..
