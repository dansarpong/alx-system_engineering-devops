# create a file in /tmp with specific requirements

file { 'create_a_file':
    path    => '/tmp/school',
    mode    => '0744',
    group   => 'www-data',
    owner   => 'www-data',
    content => 'I love Puppet',
}
