#!/usr/bin/env bash
# Bash script to setup my servers ready for the
# Deployment of web_static

# nginx installation
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/{releases/test, shared}

sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
	<head></head>
	<body>
		Fake content to test NGINX configuration
	</body>
</html>
EOF

# Creating symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# changing ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

NGINX_CONFIG='/etc/nginx/nginx.conf'
NGINX_CONFIG_BLOCK='
	server {
		location /hbnb_static {
		alias /data/web_static/current/;
		}
	}
'

# Checking if content exsists in the config file
if ! grep -qF "$NGINX_CONFIG_BLOCK" "$NGINX_CONFIG"; then
	sudo sed -i '/http {/a '"$NGINX_CONFIG_BLOCK"'' "$NGINX_CONFIG"
fi
# Restarting the nginx to apply changes
sudo service nginx restart
