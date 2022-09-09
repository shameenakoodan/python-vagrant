#Vmware fusion
Vagrant.configure("2") do |config|
  config.vm.define "pythonapp" do |pythonapp|
    pythonapp.vm.box = "spox/ubuntu-arm"
    pythonapp.vm.provider "vmware_fusion" do |vb|
      pythonapp.vm.synced_folder "app/", "/home/vagrant/app/"
      pythonapp.vm.synced_folder "env/", "/home/vagrant/env"
      vb.gui = true
    end
    pythonapp.vm.provision "shell", inline: <<-SHELL
      systemctl disable apt-daily.service
      systemctl disable apt-daily.timer
      sudo apt remove unattended-upgrades -y
    SHELL
    pythonapp.vm.provision "shell", path: "env/script.sh"
  end
end

# Virtual Box

