Vagrant.configure("2") do |config|

    # Box Settings
    config.vm.box = "ubuntu/focal64"
  
    # Provider Settings
    config.vm.provider "virtualbox" do |vb|
      # Customize the amount of memory on the VM:
      vb.memory = "1024"
      vb.cpus = "2"
    end
  
    # Network Settings
    config.vm.network "public_network", ip: "192.168.37.44"
  
    # Provision Settings
    config.vm.provision "shell", path: "bootstrap.sh"
end
  