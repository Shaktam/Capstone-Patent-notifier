echo "Creating a Bucket for Terraform State"
python3 creates3bucket.py

echo "Creating a Bucket for Patent Data"
sh patent_s3_bucket.sh

mkdir infrastructure/dbbuild

echo "zipfile for function"

cd patent-data-function/source
zip -r ../../infrastructure/dbbuild/patent-data-function.zip .
cd ../..

cd requests_layer
pip3 install -r requirements.txt --target python/lib/python3.9/site-packages
zip -r ../infrastructure/dbbuild/requests_layer.zip .
cd ..

echo "zip files for notifier"

cd patent_notifier/source
zip -r ../../infrastructure/dbbuild/notifier.zip .
cd ../..

mkdir build

echo "zip files for server"

cd patent-data-server
zip ../build/patent-data-server.zip requirements.txt
zip -r ../build/patent-data-server.zip source 
cd ..

echo  "upload to s3"
aws s3 cp build/patent-data-server.zip s3://patent-data-informer/

