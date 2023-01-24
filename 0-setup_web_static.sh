#!/usr/bin/env bash
# Write a Bash script that sets up your web servaers for the deployment of web_static. It must:
# Install Nginx if it not already installed
 apt-get update && apt-get install -y nginx

# Create the folders and files if they do not already exist
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo "<html>
    <head>
    </head>
    <body>
        ALX School
    </body>
</html>" | tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test folder and delete it if it already exists
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group, recursively
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
cat > /etc/nginx/sites-available/hbnb_static <<EOF
server {
    listen 80;
    server_name impactlight.tech;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
EOF

# Enable the new Nginx configuration
ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/

# Restart Nginx
service nginx restart
