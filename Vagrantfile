Vagrant.configure("2") do |config|
  config.vm.define "mysql" do |subconfig|
    subconfig.vm.box = "bento/centos-7.4"
    subconfig.vm.hostname = "mysql"
    subconfig.vm.network :private_network, ip: "192.168.10.142"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "docker.yml"
    end
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "mysql.yml"
    end
  end
  config.vm.define "redis" do |subconfig|
    subconfig.vm.box = "bento/centos-7.4"
    subconfig.vm.hostname = "redis"
    subconfig.vm.network :private_network, ip: "192.168.10.143"
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "docker.yml"
    end
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "redis.yml"
    end
  end
  config.vm.define "twocans1" do |subconfig|
    subconfig.vm.box = "bento/centos-7.4"
    subconfig.vm.hostname = "twocans1"
    subconfig.vm.network :private_network, ip: "192.168.10.140"
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "docker.yml"
    end
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "twocans.yml"
    end
  end
  config.vm.define "twocans2" do |subconfig|
    subconfig.vm.box = "bento/centos-7.4"
    subconfig.vm.hostname = "twocans2"
    subconfig.vm.network :private_network, ip: "192.168.10.141"
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "docker.yml"
    end
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "twocans.yml"
    end
  end
  config.vm.define "haproxy" do |subconfig|
    subconfig.vm.box = "bento/centos-7.4"
    subconfig.vm.hostname = "haproxy"
    subconfig.vm.network :private_network, ip: "192.168.10.144"
    subconfig.vm.network "forwarded_port", guest: 80, host: 8080
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "docker.yml"
    end
    subconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "haproxy.yml"
    end
  end
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
end
