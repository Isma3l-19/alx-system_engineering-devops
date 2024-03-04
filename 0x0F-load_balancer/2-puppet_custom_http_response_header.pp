# automates the task of creating a custom HTTP header response
exec { 'http header':
	command => 'sudo apt-get update -y;
		sudo apt-get install nginx -y;
		sudo sed -i "s/server_name_;\n\ntadd_header X-Served-By $HOSTNAME;\n;" /etc/nginx/sites-enabled/default;
		sudo service nginx restart',
	provider => shell,
}
