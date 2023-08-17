# Enable the user holberton to login and open a file without any error message

# Increase the hard file limit
exec { 'increase-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}

# Increase the soft file limit
exec { 'increase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}
