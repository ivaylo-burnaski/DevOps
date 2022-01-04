class install_docker {

  # simple install with all the default options
  include ::docker

  # or you can customise the install
  class { 
  'docker' :
    manage_package => true,
    package_name   => 'docker-engine',
  }

}