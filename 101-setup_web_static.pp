# puppet manifest that prepares my servers for deployment

# Executing apt-get update and apt-get install nginx
exec { 'update_apt_cache':
  command     => '/usr/bin/apt-get update',
  refreshonly => true,
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update_apt_cache'],
}

# Creating necessary directories
file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

# Creating index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>\n\t<head></head>\n\t<body>\n\t\tFake content to test NGINX configuration\n\t</body>\n</html>\n",
}

# Creating symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Changing ownership
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Adding configuration to NGINX
$nginx_config_block = "
server {
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
"

exec { 'add_nginx_config':
  command     => "/bin/echo '$nginx_config_block' >> /etc/nginx/nginx.conf",
  unless      => "/bin/grep -qF '$nginx_config_block' /etc/nginx/nginx.conf",
  require     => Package['nginx'],
  refreshonly => true,
}

# Restarting NGINX
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['add_nginx_config'],
  subscribe => File['/data/web_static/releases/test/index.html'],
}
