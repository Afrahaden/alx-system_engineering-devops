# Nginx is having many failed requests when send a high number of requests
# This increases the max number of file descriptors to handle more requests
exec { 'increase-ulimit-from-15-to-4096':
  command => 'sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}

# Restart nginx
exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}
